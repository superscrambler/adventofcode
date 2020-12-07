#!/usr/bin/python3


with open('input') as boarding_passes:

    seat_ids = {}

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
        seat_ids[int(min_row * 8 + min_col)] = True

    for seat_id in range(0, 127*8+7):
        if seat_id not in seat_ids and seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
            print(seat_id)