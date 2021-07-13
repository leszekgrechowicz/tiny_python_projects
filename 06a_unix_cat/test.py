#!/usr/bin/env python3
"""tests for cat.py.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './cat.py'
empty = './inputs/empty.txt'
one_line = './inputs/one.txt'
two_lines = './inputs/two.txt'
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
def test_one():
    """Test on file"""

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
def test_two():
    """Test on two"""

    rv, out = getstatusoutput(f'{prg} {two_lines}')
    assert rv == 0
    assert out.rstrip() == '       2       2       4 ./inputs/two.txt'


# --------------------------------------------------
def test_fox():
    """Test on fox"""

    rv, out = getstatusoutput(f'{prg} {fox}')
    assert rv == 0
    assert out.rstrip() == '       1       9      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_more():
    """Test on more than one file"""

    rv, out = getstatusoutput(f'{prg} {fox} {sonnet}')
    expected = ('       1       9      45 ../inputs/fox.txt\n'
                '      17     118     668 ../inputs/sonnet-29.txt\n'
                '      18     127     713 total')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_stdin():
    """Test on stdin"""

    rv, out = getstatusoutput(f'{prg} < {fox}')
    assert rv == 0
    assert out.rstrip() == '       1       9      45 <stdin>'


# --------------------------------------------------
def test_fox_char():
    """Test on fox with flag -c"""

    for flag in ['-c', '--char']:
        rv, out = getstatusoutput(f'{prg} {fox} {flag}')
        assert rv == 0
        assert out.rstrip() == '      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_fox_word():
    """Test on fox with flag -w"""

    for flag in ['-w', '--word']:
        rv, out = getstatusoutput(f'{prg} {fox} {flag}')
        assert rv == 0
        assert out.rstrip() == '       9 ../inputs/fox.txt'


# --------------------------------------------------
def test_fox_lines():
    """Test on fox with flag -l"""

    for flag in ['-l', '--lines']:
        rv, out = getstatusoutput(f'{prg} {fox} {flag}')
        assert rv == 0
        assert out.rstrip() == '       1 ../inputs/fox.txt'


# --------------------------------------------------
def test_fox_mix_flag_lc():
    """Test on fox with mix flag -lc"""

    for flag in ['-cl', '-lc']:
        rv, out = getstatusoutput(f'{prg} {fox} {flag}')
        assert rv == 0
        assert out.rstrip() == '       1      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_fox_mix_flag_cw():
    """Test on fox with mix flag -cw"""

    for flag in ['-cw', '-wc']:
        rv, out = getstatusoutput(f'{prg} {fox} {flag}')
        assert rv == 0
        assert out.rstrip() == '       9      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_fox_mix_flag_lw():
    """Test on fox with mix flag -lw"""

    for flag in ['-wl', '-lw']:
        rv, out = getstatusoutput(f'{prg} {fox} {flag}')
        assert rv == 0
        assert out.rstrip() == '       1       9 ../inputs/fox.txt'


# --------------------------------------------------
def test_fox_all_flag():
    """Test on fox with flag -clw"""

    for flag in ['-cwl', '-wcl', '-wlc', '-lwc', '-lcw', '-clw']:
        rv, out = getstatusoutput(f'{prg} {fox} {flag}')
        assert rv == 0
        assert out.rstrip() == '       1       9      45 ../inputs/fox.txt'
