#!/usr/bin/python3

expenses = []
with open('input') as expense_report:
    for line in expense_report:
        expenses.append(int(line))

for a in expenses:
    for b in expenses:
        for c in expenses:
            if (a + b + c) == 2020:
                print(a, b, c, a * b * c)
                quit()