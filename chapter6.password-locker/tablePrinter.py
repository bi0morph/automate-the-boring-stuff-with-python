#! /usr/bin/env python3
# tablePrinter.py - Print table

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(tableInput):
    collWidth = [0] * len(tableInput)

    for i in range(len(tableInput)):
        for j in range(len(tableInput[i])):
            word = tableInput[i][j]
            if collWidth[i] < len(word):
                collWidth[i] = len(word)

    for j in range(len(tableInput[0])):
        row = ''
        for i in range(len(tableInput)):
            word = tableInput[i][j]
            if i != 0:
                row += ' '
            row += word.rjust(collWidth[i])
        print(row)


printTable(tableData)
