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
        description='cat -- Python version',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='"Input file(s)"',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    parser.add_argument('-n',
                        '--number',
                        metavar='int',
                        type=int,
                        help="number all output lines",
                        )

    parser.add_argument('--head',
                        help="output first line",
                        action='store_true'
                        )

    parser.add_argument('-t',
                        '--tail',
                        help="number of last lines",
                        metavar='int',
                        type=int,
                        )

    parser.add_argument('-r',
                        '--reverse',
                        help="output lines in reverse order",
                        action='store_true'
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for file in args.file:
        text = file.readlines()

        print(file.name, '\n')

        if not text:
            break

        if args.reverse:
            text = text[::-1]

        if args.number:
            text = text[:args.number]

        if args.tail:
            text = text[-args.tail:]

        if args.head:
            text = text[:1]

        for line in text:
            print(line.strip())

        print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
