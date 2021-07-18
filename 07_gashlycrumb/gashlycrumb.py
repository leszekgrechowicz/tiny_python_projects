#!/usr/bin/env python3
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 2021-07-18
Purpose: Rock the Casbah
"""

import argparse
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs="+",
                        help='Letter(s)',
                        type=str)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default="gashlycrumb.txt")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    file_arg = args.file
    letters = args.letter

    file = file_arg.readlines()
    data = {sentence[0]: sentence for sentence in file}

    for i in letters:
        outcome = data.get(i.upper(), False)
        if outcome:
            print(outcome, end='')
        else:
            print(f'I do not know "{i}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
