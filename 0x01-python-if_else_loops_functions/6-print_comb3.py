#!/usr/bin/python3

for i in range(0, 10):
    for j in range(0, 10):
        if i == j:
            continue
        if i >= j:
            continue
        comma = ', ' if i*10+j != 89 else "\n"
        print("{}{}{}".format(i, j, comma), end='')
