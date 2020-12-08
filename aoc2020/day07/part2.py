#!/usr/bin/python3

rules = {}
with open('input') as rules_list:
    for line in rules_list:
        if 'contain no other bags' in line:
            continue
        outer_bag = line.split(' ')[0] + ' ' + line.split(' ')[1]
        rules[outer_bag] = {}
        for color in line.split('contain')[1].split(','):
            count = color.split(' ')[1]
            inner_bag = color.split(' ')[2] + ' ' + color.split(' ')[3]
            rules[outer_bag][inner_bag] = count

def how_many_inside(color):
    if color in rules:
        count = 0
        for inner_bag in rules[color]:
            n = int(rules[color][inner_bag])
            count += n + n * how_many_inside(inner_bag)
        return count
    else:
        return 0

print(how_many_inside('shiny gold'))