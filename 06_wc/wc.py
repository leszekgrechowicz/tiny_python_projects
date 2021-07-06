#!/usr/bin/env python3
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 2021-07-04
Purpose: Word counter
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word-count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help="Input file(s)",
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sum_bytes, sum_lines, sum_words = 0, 0, 0

    for file in args.file:
        text_bytes, text_words = 0, 0
        text = file.readlines()
        text_lines = len(text)
        for line in text:
            text_bytes += len(line)
            text_words += len(line.split())

        print(f'{text_lines:>{8}}{text_words:>{8}}{text_bytes:>{8}} {file.name}')

        sum_bytes += text_bytes
        sum_lines += text_lines
        sum_words += text_words

    if len(args.file) > 1:
        print(f'{sum_lines:>{8}}{sum_words:>{8}}{sum_bytes:>{7}} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
