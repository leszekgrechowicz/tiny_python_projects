#!/usr/bin/env python3
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 2021-06-17
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        nargs='+',
                        metavar='string',
                        help='Items(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    parser.add_argument('-n',
                        '--no_oxford',
                        help='Oxford comma disabled',
                        action='store_true')

    parser.add_argument('-c',
                        '--character',
                        help='Separation character',
                        choices=[':', '@', ';'],
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    character = args.character

    q = -1                  # comma range

    if args.no_oxford:
        q = -2

    if args.sorted:
        items.sort()

    number_of_items = len(items)

    if number_of_items > 1:
        items.insert(-1, 'and')
        if number_of_items > 2:
            text = f'{character} '.join(items[:q]) + ' ' + ' '.join(items[q:])
        else:
            text = ' '.join(items)

    else:
        text = items[0]

    print(f'You are bringing {text}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
