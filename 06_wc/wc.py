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

    parser.add_argument('-c',
                        '--char',
                        help='number of characters',
                        action='store_true')

    parser.add_argument('-l',
                        '--lines',
                        help='number of lines',
                        action='store_true')

    parser.add_argument('-w',
                        '--words',
                        help='number of words',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------

def main():
    """Count lines, words and bytes of the text from the file"""

    args = get_args()
    sum_bytes, sum_lines, sum_words = 0, 0, 0

    for file in args.file:
        text_bytes, text_words = 0, 0
        text = file.readlines()
        text_lines = len(text)
        for line in text:
            text_bytes += len(line)
            text_words += len(line.split())

        if any([args.lines, args.words, args.char]):
            report = ''

            if args.lines:
                report += f'{text_lines:>{8}}'

            if args.words:
                report += f'{text_words:>{8}}'

            if args.char:
                report += f'{text_bytes:>{8}}'

            print(report + f' {file.name}')

        else:
            print(f'{text_lines:>{8}}{text_words:>{8}}{text_bytes:>{8}} {file.name}')

        sum_bytes += text_bytes
        sum_lines += text_lines
        sum_words += text_words

    if len(args.file) > 1:
        print(f'{sum_lines:>{8}}{sum_words:>{8}}{sum_bytes:>{8}} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
