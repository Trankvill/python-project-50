#!/usr/bin/env python

import argparse

from gendiff.gendiff import generate_diff
from gendiff.formatters.formats import STYLISH


def get_args():
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration files and shows a difference'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        choices=['stylish', 'json', 'plain'],
        default=STYLISH,
        help='set format of output (default: "stylish")'
    )
    args = parser.parse_args()
    return args


def main():
    """Run generate_diff."""
    args = get_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
