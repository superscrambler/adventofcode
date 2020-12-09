#!/usr/bin/python3

ops = []
with open('input') as ops_list:
    for line in ops_list:
        ops.append(line.rstrip('\n').split(' '))

def test_program():
    acc = 0
    used = {}
    i = 0
    while True:
        if i in used or i == len(ops):
            break
        used[i] = True
        if ops[i][0] == 'acc':
            acc += int(ops[i][1])
        if ops[i][0] == 'jmp':
            i += int(ops[i][1])
        else:
            i += 1
    return (i == len(ops)), acc

for j in range(len(ops)):
    ret = False
    acc = 0
    if ops[j][0] == 'jmp':
        ops[j][0] = 'nop'
        ret,acc = test_program()
        ops[j][0] = 'jmp'
    elif ops[j][0] == 'nop':
        ops[j][0] = 'jmp'
        ret,acc = test_program()
        ops[j][0] = 'nop'
    if ret:
        print(acc)
        break