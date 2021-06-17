#!/usr/bin/env python

import argparse


def parser_():
    parser = argparse.ArgumentParser(description='Print !')
    parser.add_argument('-w', '--word', metavar='word',
                        default='Word was not given', help='Returns word you are putting here')
    return parser.parse_args()


def main():
    args = parser_()

    print(args.word)


if __name__ == '__main__':
    main()
