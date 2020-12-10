#!/usr/bin/python3

with open('input') as f:
    adapters = [0] + sorted([int(line) for line in f.readlines()])
adapters.append(adapters[-1] + 3)

cache = {}
def arrange(n):
    if n not in cache:
        if n == len(adapters) - 1:
            cache[n] = 1
        else:
            cache[n] = 0
            for j in range(1, 4):
                if n + j < len(adapters) and adapters[n + j] <= adapters[n] + 3:
                    cache[n] += arrange(n + j)
    return cache[n]

print(arrange(0))