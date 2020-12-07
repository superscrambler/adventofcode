#!/usr/bin/python3
import re

def check_passport(passport):
    if not all (key in passport for key in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
        return False
    return (re.match('^\d{4}$', passport['byr']) is not None and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002 and
            re.match('^\d{4}$', passport['iyr']) is not None and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020 and
            re.match('^\d{4}$', passport['eyr']) is not None and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030 and
            (   (re.match('^\d{3}cm$', passport['hgt']) is not None and int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193)
             or (re.match('^\d{2}in$', passport['hgt']) is not None and int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76)  ) and
            re.match('^#[0-9a-f]{6}$', passport['hcl']) is not None and
            passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and
            re.match('^\d{9}$', passport['pid']) is not None)

with open('input') as batch:
    passport = {}
    valid = 0
    for line in batch:
        if len(line) == 1:
            if check_passport(passport):
                valid += 1
            passport = {}
        else:
            for data in line.rstrip('\n').split(' '):
                key, value = data.split(':')
                passport[key] = value
    if check_passport(passport):
        valid += 1
    print(valid)