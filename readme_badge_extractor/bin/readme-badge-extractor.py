#!/usr/bin/env python3

"""Extract readme badges from readme"""

# std
import argparse

# ours
from readme_badge_extractor.extractor import DefaultExtractor
from readme_badge_extractor.badge import serialize_badges


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__file__.__doc__)
    parser.add_argument(
        "input",
        help="Input file or URL. Url has to start with http to be recognized as"
             "such."
    )
    parser.add_argument("--format", choices=["yaml", "json"], default="json")
    return parser


def is_url(input: str) -> bool:
    return input.startswith("http")


def main():
    args = get_parser().parse_args()
    de = DefaultExtractor()
    if is_url(args.input):
        badges = de.extract_from_url(args.input)
    else:
        badges = de.extract_from_file(args.input)
    print(serialize_badges(badges, format=args.format))


if __name__ == "__main__":
    main()