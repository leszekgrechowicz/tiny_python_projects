#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = os.getcwd() + './picnic.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f'{prg} chips')
    assert out.strip() == 'You are bringing chips.'


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'{prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} {arg} --sorted')
    expected = 'You are bringing apples, bananas, cherries, and dates.'
    assert out.strip() == expected


# --------------------------------------------------
def test_omit_oxford_comma():
    """more than two items Oxford comma omitting"""

    arg = 'apples bananas cherries dates'
    out = getoutput(f'{prg} {arg} --no_oxford')
    expected = 'You are bringing apples, bananas, cherries and dates.'
    assert out.strip() == expected


# --------------------------------------------------
def test_omit_oxford_comma_sorted():
    """more than two items Oxford comma omitted and sorted"""

    arg = 'apples bananas cherries dates'
    out = getoutput(f'{prg} {arg} --no_oxford --sorted')
    expected = 'You are bringing apples, bananas, cherries and dates.'
    assert out.strip() == expected


# --------------------------------------------------
def test_word_separation_option():
    """word separation character"""

    for character in [':', '@', ';']:
        arg = 'apples bananas cherries dates'
        out = getoutput(f'{prg} {arg} --character {character}')
        expected = f'You are bringing apples{character} bananas{character} cherries{character} and dates.'
        assert out.strip() == expected
