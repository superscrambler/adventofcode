#!/usr/bin/python3

with open('input') as f:
    actions = [[line[0],int(line[1:])] for line in f.readlines()]

def rotate(angle):
    if angle == 90 or angle == -270:
        return -wp_north, wp_east
    elif angle == 270 or angle == -90:
        return wp_north, -wp_east
    else:
        return -wp_east, -wp_north

ship_east = 0
ship_north = 0
wp_east = 10
wp_north = 1
for action in actions:
    if action[0] == 'N':
        wp_north += action[1]
    elif action[0] == 'S':
        wp_north -= action[1]
    elif action[0] == 'E':
        wp_east += action[1]
    elif action[0] == 'W':
        wp_east -= action[1]
    elif action[0] == 'L':
        wp_east, wp_north = rotate(action[1])
    elif action[0] == 'R':
        wp_east, wp_north = rotate(-action[1])
    else:
        ship_east += action[1] * wp_east
        ship_north += action[1] * wp_north

print(abs(ship_east) + abs(ship_north))