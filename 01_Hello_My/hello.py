#!/usr/bin/env python
"""
Author: Leszek Grechowicz leszek_grechowicz@o2.pl
Purpose: Say Hello
"""
import argparse


def get_args():
    """Check and Get command-line arguments"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """Display greetings"""
    args = get_args()
    print("Hello, " + args.name + '!')


if __name__ == '__main__':
    main()
