#!/usr/bin/env python3
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 2021-06-19
Purpose: Cipher the number
"""

import argparse
from subprocess import getstatusoutput


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Cipher the number',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Text with number to cipher')

    return parser.parse_args()


def cipher(number):
    """cipher the number if not present return number"""

    code = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5',

    }

    return code.get(number, number)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    arg_text = args.text
    coded = ''
    for character in arg_text:
        coded += cipher(character)
    print(coded)


# --------------------------------------------------
if __name__ == '__main__':
    main()
