#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 2021-06-20
Purpose: Howler (upper-cases input)
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# -------------------------------------------------

def print_upper(text):
    return text.upper()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    to_file = args.outfile
    file_exist = os.path.isfile(text)

    if file_exist and not to_file:
        with open(text) as file:
            print_upper(file.read())

    elif file_exist and to_file:
        with open(text) as file:
            print(print_upper(file.read().strip()), file=open(to_file, 'wt'))

    elif to_file:
        print(print_upper(text), file=open(to_file, 'wt'))

    else:
        print(print_upper(text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
