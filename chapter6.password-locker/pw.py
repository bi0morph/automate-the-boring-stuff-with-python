#! /usr/bin/env python3
# pw.py - An insecure password locker programme

import sys
import pyperclip

PASSWORDS = {'email': 'anything_1',
             'blog': 'something_2',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] -copy password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)