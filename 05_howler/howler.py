#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 2021-07-03
Purpose: Text upper-case output
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-case output)',
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

    par_args = parser.parse_args()
    if os.path.isfile(par_args.text):
        with open(f"{par_args.text}", 'r', encoding="utf-8") as text:
            par_args.text = text.read()

    return par_args


# --------------------------------------------------

def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.outfile:
        out_file = open(args.outfile, 'wt')
        print(args.text.upper(), file=out_file)
        out_file.close()

    else:
        print(args.text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
