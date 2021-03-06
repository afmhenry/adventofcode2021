#!/usr/bin/env python3
import csv


def countPosition(filename):
    with open(filename, encoding="latin1") as f:
        distance = 0
        depth = 0
        for index, row in enumerate(csv.reader(f, delimiter=' ')):
            operation = row[0]
            value = int(row[1])
            if operation == "forward":
                distance += value
            elif operation == "down":
                depth += value
            else:
                depth -= value

    return distance * depth


def countPositionWithAim(filename):
    with open(filename, encoding="latin1") as f:
        distance = 0
        depth = 0
        aim = 0

        for index, row in enumerate(csv.reader(f, delimiter=' ')):
            operation = row[0]
            value = int(row[1])
            if operation == "forward":
                distance += value
                depth += aim * value
            elif operation == "down":
                aim += value
            else:
                aim -= value

    return distance * depth


assert(countPosition("dec2-mock.txt") == 150)
print(countPosition("dec2.txt"))

assert(countPositionWithAim("dec2-mock.txt") == 900)
print(countPositionWithAim("dec2.txt"))
