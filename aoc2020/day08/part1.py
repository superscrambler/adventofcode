#!/usr/bin/python3

ops = []
with open('input') as ops_list:
    for line in ops_list:
        ops.append(line.rstrip('\n').split(' '))

acc = 0
used = {}
i = 0
while True:
    if i in used:
        break
    used[i] = True
    if ops[i][0] == 'acc':
        acc += int(ops[i][1])
    if ops[i][0] == 'jmp':
        i += int(ops[i][1])
    else:
        i += 1
print(acc)