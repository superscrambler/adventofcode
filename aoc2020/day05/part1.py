#!/usr/bin/python3

with open('input') as boarding_passes:
    max_seat_id = 0
    for bsp in boarding_passes:
        min_row = 0
        max_row = 127
        for x in bsp[:7]:
            if x == 'F':
                max_row = min_row + (max_row - min_row + 1) / 2 - 1
            else:
                min_row = min_row + (max_row - min_row + 1) / 2
        min_col = 0
        max_col = 7
        for y in bsp[7:10]:
            if y == 'L':
                max_col = min_col + (max_col - min_col + 1) / 2 - 1
            else:
                min_col = min_col + (max_col - min_col + 1) / 2
        seat_id = int(min_row * 8 + min_col)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    print(max_seat_id)