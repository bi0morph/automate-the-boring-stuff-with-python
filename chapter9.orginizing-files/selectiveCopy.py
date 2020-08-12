#! /usr/bin/env python3
# selectiveCopy.py - Walks through a folder tree and searches for files with a certain file extension and
# copy them to a new folder

import os
import sys
import re
import shutil

def copyFiles(folder, extension, destinationFolder = '.'):
    print('Check files in %s for %s extension' % (folder, extension))

    if not os.path.exists(destinationFolder):
        print('Folder %s does not exist and it will be created')
        try:
            os.mkdir(destinationFolder)
        except OSError:
            print('Creation of the directory %s failed' % destinationFolder)
            sys.exit(1)
        else:
            print('Successfully created the directory %s' % destinationFolder)
    elif not os.path.isdir(destinationFolder):
        print('Destination is not a folder')
        sys.exit(1)

    extRegExp = re.compile(r'(.*)' + extension)
    copied = 0
    for foldername, subfolder, filenames in os.walk(folder):
        print('Looking in %s...' % foldername)
        for filename in filenames:

            if extRegExp.match(filename):
                fillFilename = os.path.join(foldername, filename)
                destinationFilename = os.path.join(destinationFolder, filename)
                print('Copy "%s" to "%s"' % (fillFilename, destinationFilename))
                shutil.copy(fillFilename, destinationFilename)
                copied += 1
    print('Copied %s files' % copied)


copyFiles('./chapter8.files-r&w', '.py', './chapter8-copy')