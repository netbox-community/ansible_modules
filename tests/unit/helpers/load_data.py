# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Helper functions for loading structured test data for unit tests.

Provides functions to locate JSON test_data files based on the
location of the test script in tests/unit/ and to return the data
as lists of tuples for use in pytest parameterization.
"""

import json
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()  # Current file abs path
UNIT_TESTS_DIR = CURRENT_FILE.parents[1]  # project_root/tests/unit
# Relative path from project root to unit tests dir - tests/unit
ROOT_TO_UNIT_TESTS = CURRENT_FILE.parents[1].relative_to(CURRENT_FILE.parents[3])


def load_test_data(script_dir: Path, file_name: str, use_subfold: bool = True) -> list:
    """
    Load structured test data for a test file.

    The directory structure is derived from:
    tests/unit/<unit_test_dir>/<optional_subfolder>/...

    Args:
        test_script_dir: Directory containing the test file.
        file_name: Name of the test_data folder to load.
        use_sub: Dive into same subfolders as script_dir in test_data

    Returns:
        List of tuples extracted from the JSON file.
    """
    try:
        # Normal environments: script_dir is resolved under same path tests/unit
        units_to_test_file: list = script_dir.relative_to(UNIT_TESTS_DIR).parts
    except ValueError:
        # Fallback for tox/CI virtual environments where path tests/unit differ
        # Find the path fragment "tests/unit" and slice from there
        parts = list(script_dir.parts)
        try:
            idx = parts.index(UNIT_TESTS_DIR.parts[-1])  # project/tests/unit/...
            units_to_test_file: list = parts[idx + 1 :]
        except ValueError:
            # Last-resort fallback: treat as having no subfolder
            units_to_test_file = ()

    unit_test_dir: str = units_to_test_file[0] if len(units_to_test_file) > 0 else ""
    subfolder = Path(*units_to_test_file[1:]) if len(units_to_test_file) > 1 else None

    # Build data.json path
    base = ROOT_TO_UNIT_TESTS / unit_test_dir / "test_data"
    if subfolder and use_subfold:
        base /= subfolder

    data_file = base / f"{file_name}.json"

    with data_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    return [tuple(item.values()) for item in data]
