#!/usr/bin/python3

with open('input') as cdfs:
    answers = []
    count = 0
    answers.append({})
    j = 1
    for line in cdfs:
        if line == '\n':
            count += 1
            answers.append({})
            j = 1
        else:
            answers[count][j] = line.rstrip('\n')
            j += 1
    sum = 0
    for g in range(count + 1):
        for p in range(2, len(answers[g]) + 1):
            common = ''
            for l in answers[g][1]:
                if l in answers[g][p]:
                    common += l
            answers[g][1] = common
        sum += len(answers[g][1])
    print(sum)