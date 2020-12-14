#!/usr/bin/python3

with open('input') as f:
    actions = [[line[0],int(line[1:])] for line in f.readlines()]

def turn(d, n):
    d += n
    if d >= 360:
        d -= 360
    if d < 0:
        d += 360
    return d

east = 0
north = 0
direction = 90
for action in actions:
    if action[0] == 'N' or (action[0] == 'F' and direction == 0):
        north += action[1]
    elif action[0] == 'S' or (action[0] == 'F' and direction == 180):
        north -= action[1]
    elif action[0] == 'E' or (action[0] == 'F' and direction == 90):
        east += action[1]
    elif action[0] == 'W' or (action[0] == 'F' and direction == 270):
        east -= action[1]
    elif action[0] == 'L':
        direction = turn(direction, -action[1])
    elif action[0] == 'R':
        direction = turn(direction, action[1])

print(abs(east) + abs(north))