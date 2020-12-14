#!/usr/bin/python3

with open('input') as f:
    seats = [list(line.rstrip('\n')) for line in f.readlines()]

directions = []
for r in [-1, 0, 1]:
    for c in [-1, 0, 1]:
        if r !=0 or c != 0:
            directions.append([r, c])

def occupied(row, col):
    count = 0
    for d in directions:
        r = row + d[0]
        c = col + d[1]
        while r >= 0 and r < len(seats) and c >= 0 and c < len(seats[0]):
            if seats[r][c] == '#':
                count += 1
                break
            if seats[r][c] == 'L':
                break
            r += d[0]
            c += d[1]
    return count

def round():
    new_seats = [row[:] for row in seats]
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            if seats[r][c] == 'L' and occupied(r,c) == 0:
                new_seats[r][c] = '#'
            elif seats[r][c] == '#' and occupied(r,c) >= 5:
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