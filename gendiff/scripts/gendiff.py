#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(
            usage='gendiff [-h] [-f FORMAT] first_file second_file',
            description='Compares two configuration files and shows a difference'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    #parser.print_help()
    args = parser.parse_args()
    print(args.first_file, args.second_file)

if __name__=='__main__':
    main()
