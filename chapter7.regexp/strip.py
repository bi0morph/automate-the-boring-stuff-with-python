#! /usr/bin/env python
# strip.py - strip string but with regexp

import re


def strip(value, replace=''):
    return re.compile(r'(^\s+)|(\s+)$').sub(replace, value)