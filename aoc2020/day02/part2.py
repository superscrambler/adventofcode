#!/usr/bin/python3

with open('input') as password_list:
    passwords = []
    valid = 0
    for line in password_list:
        numbers, letter, password = line.split(' ')
        pos1, pos2 = numbers.split('-')
        occ = 0
        if password[int(pos1) - 1] == letter[0]:
            occ = occ + 1
        if password[int(pos2) - 1] == letter[0]:
            occ = occ + 1
        if occ == 1:
            valid = valid + 1
    print(valid)