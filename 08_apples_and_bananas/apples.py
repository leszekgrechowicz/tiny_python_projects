#!/usr/bin/env python3
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 2021-07-18
Purpose: Rock the Casbah
"""

import argparse
from os import path


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=['a', 'e', 'i', 'o', 'u'])

    out = parser.parse_args()

    if path.isfile(out.text):
        out.text = open(f'{out.text}').read()

    return out


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    choices = ['a', 'e', 'i', 'o', 'u']

    args = get_args()

    text = args.text

    text_out = ''

    for i in text:
        vowel = args.vowel
        upper = False

        if i.isupper():
            upper = True

        if upper:
            vowel = vowel.upper()

        if i.lower() in choices:
            text_out += vowel
        else:
            text_out += i

    print(text_out)


# --------------------------------------------------
if __name__ == '__main__':
    main()
