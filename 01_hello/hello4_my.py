#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Say Hello')
parser.add_argument('-n', '--name', metavar='name',
                     help='Name to greet')

args = parser.parse_args()

print(f'Hello {args.name}!')
