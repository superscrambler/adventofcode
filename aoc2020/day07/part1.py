#!/usr/bin/python3

rules = {}
with open('input') as rules_list:
    for line in rules_list:
        if 'contain no other bags' in line:
            continue
        outer_bag = line.split(' ')[0] + ' ' + line.split(' ')[1]
        for color in line.split('contain')[1].split(','):
            inner_bag = color.split(' ')[2] + ' ' + color.split(' ')[3]
            if inner_bag not in rules:
                rules[inner_bag] = []
            rules[inner_bag].append(outer_bag)

possible = {}
def which_bag(color):
    if color in rules:
        for outer_bag in rules[color]:
            possible[outer_bag] = True
            which_bag(outer_bag)

which_bag('shiny gold')
print(len(possible))