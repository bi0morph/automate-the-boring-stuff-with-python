#! /usr/bin/env python3
# mapIt.py - Translate word or sentence from command line or clipboard.

import webbrowser
import sys
import pyperclip
import re

if len(sys.argv) > 1:
    # Get text from command line
    text = ' '.join(sys.argv[1:])
else:
    # Get text from clipboard.
    text = pyperclip.paste()

text = re.compile(r'(\s+)').sub('%20', text)
webbrowser.open('https://translate.google.com/#view=home&op=translate&sl=auto&tl=ru&text=' + text).encode('utf-8')