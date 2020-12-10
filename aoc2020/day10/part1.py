#!/usr/bin/python3

with open('input') as f:
    adapters = sorted([int(line) for line in f.readlines()])

c1 = 0
c3 = 0
jolts = 0
for adapter in adapters:
    if adapter == jolts + 1:
        c1 += 1
    elif adapter == jolts + 3:
        c3 += 1
    jolts = adapter
print(c1 * (c3 + 1))