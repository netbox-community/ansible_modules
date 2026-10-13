#!/usr/bin/env bash
#
# Provision a NetBox v2 API token via POST /api/users/tokens/provision/.
#
# Used by CI (and local dev) against NetBox v4.5+, which creates v2 tokens by
# default. v2 tokens cannot be pre-seeded via SUPERUSER_API_TOKEN and must be
# obtained at runtime using superuser credentials.
#
# Outputs the full token (nbt_<KEY>.<TOKEN>) on stdout and writes it to
# /tmp/.netbox_test_token (chmod 600) and /tmp/netbox-token.env (sourceable).
#
set -euo pipefail

for dep in curl jq; do
    command -v "$dep" >/dev/null 2>&1 || {
        printf 'ERROR: %s not found in PATH\n' "$dep" >&2
        exit 1
    }
done

NETBOX_URL="${NETBOX_URL:-http://localhost:32768}"
NETBOX_USERNAME="${NETBOX_USERNAME:-admin}"
NETBOX_PASSWORD="${NETBOX_PASSWORD:-admin123456}"
MAX_RETRIES="${MAX_RETRIES:-30}"
RETRY_DELAY="${RETRY_DELAY:-5}"
TOKEN_FILE="${TOKEN_FILE:-/tmp/.netbox_test_token}"
TOKEN_ENV_FILE="${TOKEN_ENV_FILE:-/tmp/netbox-token.env}"

log() { printf '%s\n' "$*" >&2; }

log "Waiting for NetBox at $NETBOX_URL ..."
for i in $(seq 1 "$MAX_RETRIES"); do
    # `|| echo "000"` keeps transient connection-refused / timeout failures
    # from exiting the script via `set -e` before the retry loop gets to retry.
    status=$(curl -s -o /dev/null -m 5 -w '%{http_code}' "$NETBOX_URL/login/" || echo "000")
    if [ "$status" = "200" ]; then
        log "NetBox is ready."
        break
    fi
    if [ "$i" -eq "$MAX_RETRIES" ]; then
        log "ERROR: NetBox did not become ready within $((MAX_RETRIES * RETRY_DELAY))s (last status: $status)."
        exit 1
    fi
    log "  attempt $i/$MAX_RETRIES got status=$status, sleeping ${RETRY_DELAY}s"
    sleep "$RETRY_DELAY"
done

log "Provisioning v2 API token for user '$NETBOX_USERNAME' ..."
# Build the JSON body with jq rather than string interpolation so credentials
# containing quotes / backslashes / newlines can't break the request payload.
BODY=$(jq -n --arg u "$NETBOX_USERNAME" --arg p "$NETBOX_PASSWORD" \
    '{username: $u, password: $p}')
RESPONSE=$(curl -s -X POST \
    --connect-timeout 10 -m 30 \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    "$NETBOX_URL/api/users/tokens/provision/" \
    --data "$BODY")

if ! echo "$RESPONSE" | jq -e . >/dev/null 2>&1; then
    log "ERROR: token provisioning returned non-JSON response:"
    log "$RESPONSE"
    exit 1
fi

if echo "$RESPONSE" | jq -e 'has("detail") or has("error")' >/dev/null; then
    log "ERROR: token provisioning rejected:"
    echo "$RESPONSE" | jq . >&2
    exit 1
fi

KEY=$(echo "$RESPONSE" | jq -r '.key // empty')
TOKEN=$(echo "$RESPONSE" | jq -r '.token // empty')
VERSION=$(echo "$RESPONSE" | jq -r '.version // empty')

if [ -z "$KEY" ] || [ -z "$TOKEN" ] || [ "$VERSION" != "2" ]; then
    log "ERROR: unexpected provisioning response (expected v2 token with key+token):"
    echo "$RESPONSE" | jq . >&2
    exit 1
fi

FULL_TOKEN="nbt_${KEY}.${TOKEN}"

# Remove any pre-existing file first; `printf > file` preserves the existing
# mode on truncation, so without this the chmod-600 claim below is unreliable.
rm -f "$TOKEN_FILE" "$TOKEN_ENV_FILE"
umask 077
printf '%s' "$FULL_TOKEN" > "$TOKEN_FILE"
printf 'export NETBOX_TOKEN=%q\n' "$FULL_TOKEN" > "$TOKEN_ENV_FILE"
chmod 600 "$TOKEN_FILE" "$TOKEN_ENV_FILE"

log "Provisioned v2 token (key=$KEY), written to $TOKEN_FILE and $TOKEN_ENV_FILE."
echo "$FULL_TOKEN"
