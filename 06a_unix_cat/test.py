#!/usr/bin/env python3
"""tests for cat.py.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './cat.py'
empty = './inputs/empty.txt'
one_file = './inputs/one.txt'
two_files = './inputs/one.txt ./inputs/two.txt'
fox = '../inputs/fox.txt'
preamble = '../inputs/preamble.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_bad_file():
    """bad_file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_empty():
    """Test on empty"""

    rv, out = getstatusoutput(f'{prg} {empty}')
    assert rv == 0
    assert out.rstrip() == './inputs/empty.txt'


# --------------------------------------------------
def test_one_file():
    """Test on one file"""

    rv, out = getstatusoutput(f'{prg} {preamble}')
    assert rv == 0
    assert out == """../inputs/preamble.txt 

When, in the course of human events, it becomes necessary for one people to
dissolve the political bands which have connected them with another, and to
assume among the powers of the earth, the separate and equal station to
which the laws of nature and of nature's God entitle them, a decent respect
to the opinions of mankind requires that they should declare the causes
which impel them to the separation.
"""


# --------------------------------------------------
def test_two_files():
    """Test on two files"""

    rv, out = getstatusoutput(f'{prg} {two_files}')
    assert rv == 0
    assert out.rstrip() == """./inputs/one.txt 

1 this is first line from file one
2 this is second line from file one
3 this is third line from file one
4 this is fourth line from file one
5 this is fifth line from file one
6 this is sixth line from file one

./inputs/two.txt 

1 this is first line from file two
2 this is second line from file two
3 this is third line from file two
4 this is fourth line from file two
5 this is fifth line from file two
6 this is sixth line from file two"""


# --------------------------------------------------
def test_one_file_reversed():
    """Test on one file option reversed """

    rv, out = getstatusoutput(f'{prg} {one_file} -r')
    assert rv == 0
    assert out.rstrip() == """./inputs/one.txt 

6 this is sixth line from file one
5 this is fifth line from file one
4 this is fourth line from file one
3 this is third line from file one
2 this is second line from file one
1 this is first line from file one"""


# --------------------------------------------------
def test_two_files_reversed():
    """Test on two files option reversed """

    rv, out = getstatusoutput(f'{prg} {two_files} -r')
    assert rv == 0
    assert out.rstrip() == """./inputs/one.txt 

6 this is sixth line from file one
5 this is fifth line from file one
4 this is fourth line from file one
3 this is third line from file one
2 this is second line from file one
1 this is first line from file one

./inputs/two.txt 

6 this is sixth line from file two
5 this is fifth line from file two
4 this is fourth line from file two
3 this is third line from file two
2 this is second line from file two
1 this is first line from file two"""


# --------------------------------------------------
def test_one_file_number_of_lines_reversed():
    """Test on one file with option reversed and number of lines"""

    rv, out = getstatusoutput(f'{prg} {one_file} -rn 3')
    assert rv == 0
    assert out.rstrip() == """./inputs/one.txt 

6 this is sixth line from file one
5 this is fifth line from file one
4 this is fourth line from file one"""


# --------------------------------------------------
def test_stdin():
    """Test on stdin"""

    rv, out = getstatusoutput(f'{prg} < {fox}')
    assert rv == 0
    assert out.rstrip() == """<stdin> 

The quick brown fox jumps over the lazy dog."""


# --------------------------------------------------
def test_one_file_head():
    """Test on one option head"""

    rv, out = getstatusoutput(f'{prg} {one_file} --head')
    assert rv == 0
    assert out.rstrip() == """./inputs/one.txt 

1 this is first line from file one"""


# --------------------------------------------------
def test_one_file_tail():
    """Test on one file number of last lines"""

    for flag in ['-t', '--tail']:
        rv, out = getstatusoutput(f'{prg} {one_file} {flag} 3')
        assert rv == 0
        assert out.rstrip() == """./inputs/one.txt 

4 this is fourth line from file one
5 this is fifth line from file one
6 this is sixth line from file one"""
