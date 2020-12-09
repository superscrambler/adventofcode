#!/usr/bin/python3

numbers = []
with open('input') as numbers_list:
    for line in numbers_list:
        numbers.append(int(line.rstrip('\n')))

preamble = 25
for n in range(preamble, len(numbers)):
    previous = []
    for i in range(n - preamble, n):
        previous.append(numbers[i])
    match = False
    for j in previous:
        for k in previous:
            if j != k and j + k == numbers[n]:
                match = True
    if not match:
        break
print(numbers[n])