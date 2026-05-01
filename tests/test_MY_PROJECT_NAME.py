"""Tests for MY_PROJECT_NAME package."""

from __future__ import annotations

import MY_PROJECT_NAME


def test_version_is_string() -> None:
    assert isinstance(MY_PROJECT_NAME.__version__, str)


def test_version_has_three_parts() -> None:
    parts = MY_PROJECT_NAME.__version__.split(".")
    assert len(parts) == 3
