#!/usr/bin/python3

import re

required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

with open('input') as batch:
    passport = {}
    valid = 0
    for line in batch:
        if len(line) == 1:
            if all (key in passport for key in required):
                valid += 1
            passport = {}
        else:
            for data in line.rstrip('\n').split(' '):
                key, value = data.split(':')
                passport[key] = value
    if all (key in passport for key in required):
        valid += 1
    print(valid)