#! /usr/bin/env python3
# regex-search.py - Opens all .txt files in folder and search by users regex
# Usage: ./regex-search.py ./folder Bat\w{4:}

import re
import sys
import os
if len(sys.argv) == 3:
    folderPath = sys.argv[1]
    regexString = sys.argv[2]
    if os.path.isdir(folderPath):
        regExObj = re.compile(r''+regexString)
        print('Searching text in the %s for "%s"...' % (folderPath, regexString))
        files = os.listdir(folderPath)
        matches = []
        for fileName in files:
            if re.compile(r'.txt$').search(fileName):
                matchesInFile = []
                file = open(os.path.join(folderPath, fileName), 'r')
                for line in file.readlines():
                    results = regExObj.findall(line)
                    if len(results) > 0:
                        print('File %s. Found %s' % (fileName, str(len(results))))
                        matches = matches + results
        if len(matches) > 0:
            print('Results')
            for result in matches:
                print(result)
        else:
            print('Nothing was found.')
    else:
        print('Provider folder path is not a folder')
else:
    print('Provide first argument with a folder and second argument with regex string')

