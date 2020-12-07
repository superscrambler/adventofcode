#!/usr/bin/python3

with open('input') as password_list:
    passwords = []
    valid = 0
    for line in password_list:
        numbers, letter, password = line.split(' ')
        minimum, maximum = numbers.split('-')
        count = 0
        for a in password:
            if a == letter[0]:
                count = count + 1
        if count >= int(minimum) and count <= int(maximum):
            valid = valid + 1
    print(valid)