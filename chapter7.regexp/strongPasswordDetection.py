#! /usr/bin/env python
# strongPasswordDetection - Check that password meets requirements
# at least eight character long
# contains both uppercase and lowercase characters
# has at least one digit

import sys, re

if len(sys.argv) < 2:
    print('Usage: python strongPasswordDetection.py [password] - check password')
    sys.exit()


def verifyPassword(pwd):
    atLeastEightChar = re.compile('\w{8,}')
    atLeastOneDigit = re.compile('\d+')
    atLeastOneUppercase = re.compile('[A-Z]+')
    atLeastOneLowercase = re.compile('[a-z]+')
    patterns = [atLeastEightChar, atLeastOneDigit, atLeastOneUppercase, atLeastOneLowercase]
    for i in range(len(patterns)):
        if not patterns[i].search(pwd):
            return False
    return True

password = sys.argv[1]
if verifyPassword(password):
    print('Password is good enough')
else:
    print('Weak password. Try better')