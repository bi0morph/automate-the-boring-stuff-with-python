#! /usr/bin/env python3
# fillingInTheGaps.py - Finds all files with a given prefix and locates any gaps in the numbering and
# rename all files to fill these gaps
# Usage: python fillingInTheGaps.py [folder] [prefix] [numSize]
# Example: ./fillingInTheGaps.py  ./gaps-examples spam 3

import os
import sys
import re
import shutil

if len(sys.argv) < 3:
    print('Usage: python fillingInTheGaps.py [folder] [prefix] [numSize]')
    sys.exit()

folder = sys.argv[1]
prefix = sys.argv[2]
numSize = int(sys.argv[3])

if not os.path.isdir(folder):
    print('%s is not a folder' % folder)
    sys.exit(1)

regexString = '^(' + prefix + ')(\\d+)(.*?)'
pattern = re.compile(regexString)
files = {}
filesNum = []

files = []
fileNumbers = []
for filename in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, filename)):
        nameGroups = pattern.search(filename)
        if nameGroups:
            files.append(filename)
            fileNumbers.append(nameGroups.group(2))

files = sorted(files)
for i in range(len(files)):
    num = str(int(i) + 1)
    num = num.rjust(numSize, '0')
    if num not in fileNumbers:
        lastFile = files.pop()
        missedFileName = '%s%s.txt' % (prefix, num)
        fromFile = os.path.join(folder, lastFile)
        toFile = os.path.join(folder, missedFileName)
        print('Moving %s to %s' % (fromFile, toFile))
        fileNumbers.append(num)
        shutil.move(fromFile, toFile)

print('Done.')
