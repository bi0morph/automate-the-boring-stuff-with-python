#! /usr/bin/env python3
# mcb.py - Saves and loads pieces of text to the clipboard.
# Usage: py.exe myb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe myb.pyw delete <keyword> - Deletes saved keyword.
#        py.exe myb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe myb.pyw list - Loads all keywords to clipboard.

import shelve
import sys
import pyperclip

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        mcbShelf.clear()
        # for k in mcbShelf.keys():
        #     del mcbShelf[k]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print('Nothing to copy')

mcbShelf.close()
