import argparse

from dundie.core import load  # noqa


def main():
    parse = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog="Enjoy and use with cautious",
    )
    parse.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
    )
    parse.add_argument(
        "filepath",
        type=str,
        help="File path to load",
    )
    args = parse.parse_args()

    print(*globals()[args.subcommand](args.filepath))
