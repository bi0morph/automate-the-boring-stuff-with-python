#! /usr/bin/env python3
# madlibs.py - Convert text template to text

import re

# open file and get text
textFile = open('./mad-lab/text.txt', 'r')
text = textFile.read()

# ask to replace ADJECTIVE
print('Enter the adjective:')
adjective = input()
text = re.compile('ADJECTIVE').sub(adjective, text)

# ask to replace NOUN
print('Enter the noun:')
noun = input()
text = re.compile('NOUN').sub(noun, text)

# ask to replace VERB
print('Enter the verb:')
verb = input()
text = re.compile('VERB').sub(verb, text)


resultFile = open('./mad-lab/result.txt', 'w')
resultFile.write(text)
print('New text generated:\n' + text)