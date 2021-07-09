#!/usr/bin/env python3
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 2021-07-08
Purpose: cat (Unix/Linux) python version
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='cat Python version',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='"Input file(s)"',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)
    file_arg = args.file


# --------------------------------------------------
if __name__ == '__main__':
    main()
