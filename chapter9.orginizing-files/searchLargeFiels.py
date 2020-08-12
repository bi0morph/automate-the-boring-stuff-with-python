#! /usr/bin/env python
# searchLargeFiles.py - Walks through a folder tree and searches fro exceptionally large files or folders
# Usage: ./searchLargeFiles.py folder

import os
import sys

if len(sys.argv) < 2:
    print('Usage: python searchLargeFiles.py [folder]')
    sys.exit()

folder = sys.argv[1]

if not os.path.isdir(folder):
    print('%s is not a folder' % folder)
    sys.exit(1)

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        filePath = os.path.join(foldername, filename)
        size = os.path.getsize(filePath)

        # 100MB
        if size > 100*1024*1024:
            print('Large file %s' % filePath)
