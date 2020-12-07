#!/usr/bin/python3

slopex = [ 1, 3, 5, 7, 1 ]
total = 1

for i, sx in enumerate(slopex):
    with open('input') as treemap:
        x = 0
        trees = 0
        for j, line in enumerate(treemap):
            if i == 4 and (j % 2) != 0:
                continue
            w = len(line) - 1
            if line[x] == '#':
                trees = trees + 1
            x = x + sx
            if x >= w:
                x = x - w
        total = total * trees
    print(total)