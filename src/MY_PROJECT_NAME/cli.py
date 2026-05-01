"""CLI entry point for MY_PROJECT_NAME."""

from __future__ import annotations

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argument parser."""
    parser = argparse.ArgumentParser(
        prog="MY_PROJECT_NAME",
        description="MY_PROJECT_NAME command-line interface.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {_get_version()}",
    )
    subparsers = parser.add_subparsers(dest="command", metavar="<command>")

    # Example sub-command: greet
    greet_parser = subparsers.add_parser("greet", help="Print a greeting.")
    greet_parser.add_argument("name", help="Name to greet.")
    greet_parser.add_argument(
        "--shout",
        action="store_true",
        default=False,
        help="Print in uppercase.",
    )

    return parser


def _get_version() -> str:
    from MY_PROJECT_NAME import __version__

    return __version__


def cmd_greet(name: str, *, shout: bool = False) -> None:
    """Execute the greet sub-command."""
    message = f"Hello, {name}!"
    print(message.upper() if shout else message)


def main(argv: list[str] | None = None) -> int:
    """Main entry point; returns an exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "greet":
        cmd_greet(args.name, shout=args.shout)
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
