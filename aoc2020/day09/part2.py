#!/usr/bin/python3

numbers = []
with open('input') as numbers_list:
    for line in numbers_list:
        numbers.append(int(line.rstrip('\n')))

invalid = 104054607

for n in range(len(numbers)):
    count = numbers[n]
    for m in range(n + 1, len(numbers)):
        count += numbers[m]
        if count >= invalid:
            break
    if count == invalid:
        min = numbers[n]
        max = numbers[n]
        for i in range(n, m):
            if numbers[i] < min:
                min = numbers[i]
            if numbers[i] > max:
                max = numbers[i]
        print(min + max)
        break