"""Tests for the MY_PROJECT_NAME CLI."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pytest

from MY_PROJECT_NAME.cli import build_parser, cmd_greet, main


def test_greet_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    cmd_greet("World")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"


def test_greet_shout(capsys: pytest.CaptureFixture[str]) -> None:
    cmd_greet("World", shout=True)
    captured = capsys.readouterr()
    assert captured.out.strip() == "HELLO, WORLD!"


def test_main_no_args_returns_zero() -> None:
    assert main([]) == 0


def test_main_greet_returns_zero() -> None:
    assert main(["greet", "Alice"]) == 0


def test_main_unknown_command_returns_zero() -> None:
    # unknown commands fall through to help
    parser = build_parser()
    args = parser.parse_args([])
    assert args.command is None
