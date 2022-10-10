#!/usr/bin/env python

import argparse
from gendiff.gendiff import generate_diff
from gendiff.formatters.formats import JSON


def main():
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration files and shows a difference'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default=JSON,
        help='set format of output'
    )
    args = parser.parse_args()
    print(str(generate_diff(args.first_file, args.second_file)))


if __name__ == '__main__':
    main()
