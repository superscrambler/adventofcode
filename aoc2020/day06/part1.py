#!/usr/bin/python3

with open('input') as cdfs:
    answers = []
    count = 0
    answers.append({})
    for line in cdfs:
        if len(line) == 1:
            count += 1
            answers.append({})
        else:
            for x in line.rstrip('\n'):
                answers[count][x] = True
    sum = 0
    for g in range(count + 1):
        sum += len(answers[g])
    print(sum)