"""
Custom super_user.py for CI testing with NetBox v4.5+

Creates a v1 (legacy) API token so that existing integration tests
can authenticate with the static token value using the "Token <value>"
header format.  v1 tokens remain supported in NetBox v4.5 (removal
scheduled for v4.7).
"""

from os import environ

from users.choices import TokenVersionChoices
from users.models import Token, User


def _read_secret(secret_name, default=None):
    try:
        f = open("/run/secrets/" + secret_name, "r", encoding="utf-8")
    except EnvironmentError:
        return default
    else:
        with f:
            return f.readline().strip()


su_name = environ.get("SUPERUSER_NAME", "admin")
su_email = environ.get("SUPERUSER_EMAIL", "admin@example.com")
su_password = _read_secret(
    "superuser_password", environ.get("SUPERUSER_PASSWORD", "admin")
)
su_api_token = _read_secret(
    "superuser_api_token",
    environ.get("SUPERUSER_API_TOKEN", "0123456789abcdef0123456789abcdef01234567"),
)

if not User.objects.filter(username=su_name).exists():
    u = User.objects.create_superuser(su_name, su_email, su_password)
    Token.objects.create(user=u, token=su_api_token, version=TokenVersionChoices.V1)
    print(
        f"💡 Superuser Username: {su_name}, E-Mail: {su_email},"
        f" API Token (v1): {su_api_token}"
    )
