#!/usr/bin/env python3
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 2021-06-13
Purpose: Choose the correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the correct article ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('mandatory',
                        metavar='word',
                        type=str,
                        help='A word - mandatory')

    parser.add_argument('-s', '--starboard',
                        action='store_true',
                        help='changes the side to “starboard”')

    return parser.parse_args()


# --------------------------------------------------
def make_sentence(word, side):
    """Produce sentence with appropriate article to the word given"""

    article = 'an' if word[0].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'

    if word[0].istitle():
        article = article.title()

    return f'Ahoy, Captain, {article} {word} off the {side} bow!'


# --------------------------------------------------

def main():
    """Make a jazz noise here"""

    args = get_args()
    side = 'starboard' if args.starboard else 'larboard'
    mandatory_arg = args.mandatory

    print(make_sentence(mandatory_arg, side))


# --------------------------------------------------
if __name__ == '__main__':
    main()
