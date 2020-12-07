#!/usr/bin/python3

with open('input') as treemap:
    x = 0
    trees = 0
    for line in treemap:
        w = len(line) - 1
        if line[x] == '#':
            trees = trees + 1
        x = x + 3
        if x >= w:
            x = x - w
    print(trees)