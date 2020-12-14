#!/usr/bin/python3

with open('input') as f:
    seats = [list(line.rstrip('\n')) for line in f.readlines()]

def occupied(row, col):
    count = 0
    for r in range(max(0, row - 1), min(row + 2, len(seats))):
        for c in range(max(0, col -1), min(col + 2, len(seats[0]))):
            if r != row or c != col:
                if seats[r][c] == '#':
                    count += 1
    return count

def round():
    new_seats = [row[:] for row in seats]
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            if seats[r][c] == 'L' and occupied(r,c) == 0:
                new_seats[r][c] = '#'
            elif seats[r][c] == '#' and occupied(r,c) >= 4:
                new_seats[r][c] = 'L'
    return new_seats

def seats_id():
    id = ""
    for row in seats:
        s = ""
        id += s.join(row)
    return id

id1 = seats_id()
while True:
    seats = [row[:] for row in round()]
    id2 = seats_id()
    if id1 == id2:
        break
    else:
        id1 = id2

count = 0
for row in seats:
    for seat in row:
        if seat == "#":
            count += 1

print(count)