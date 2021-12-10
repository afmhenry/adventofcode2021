#!/usr/bin/env python3
import csv
import math
import pandas as pd
import copy
from threading import Thread


def is_greater(val, y):
    return False if val >= y else True


def pathfinder(filename):
    count = 0
    with open(filename, encoding="latin1") as f:
        height = len(f.readline()) - 1
        width = sum(1 for row in csv.reader(f, delimiter=" ")) + 1
        mapping = [[0 for i in range(height)] for j in range(width)]

        data = pd.read_csv(filename, header=None)
        data = data.to_numpy()

        i = 0
        for _ in data:
            for row in _:
                j = 0
                for value in str(row):
                    mapping[i][j] = int(value)
                    j += 1
                i += 1

        # print(mapping)
        # printPretty(mapping)
        mins = []
        risk_level = 0
        for row in range(len(mapping)):
            for col in range(len(mapping[row])):
                is_min = True
                # first look left and right
                if row - 1 in range(width):
                    is_min = is_greater(mapping[row][col], mapping[row - 1][col])
                if is_min and row + 1 in range(width):
                    is_min = is_greater(mapping[row][col], mapping[row + 1][col])
                # then look up and down
                if is_min and col - 1 in range(height):
                    is_min = is_greater(mapping[row][col], mapping[row][col - 1])
                if is_min and col + 1 in range(height):
                    is_min = is_greater(mapping[row][col], mapping[row][col + 1])
                if is_min:
                    mins.append((row, col))
                    risk_level += mapping[row][col] + 1

        basins = []

        for (row, col) in mins:
            basin = [(row, col)]
            findBasin(row, col, basin, mapping, height, width)
            basins.append(len(basin))
        basins.sort()

        result = 1
        for i in range(3):
            result *= basins[len(basins) - (i + 1)]

        return result


def findBasin(row, col, basin, mapping, height, width):
    mapping[row][col] = 9
    adjacent_position = [
        (row, col - 1),
        (row, col + 1),
        (row + 1, col),
        (row - 1, col)
    ]

    for pos in adjacent_position:
        if pos[0] in range(width) and \
                pos[1] in range(height) and \
                mapping[pos[0]][pos[1]] != 9:
            basin.append((pos[0], pos[1]))
            findBasin(pos[0], pos[1], basin, mapping, height, width)
    return basin


def printPretty(two_dim_array):
    for row in two_dim_array:
        print(row)


print(pathfinder("dec9-mock.txt"))
assert (pathfinder("dec9-mock.txt") == 1134)

print(pathfinder("dec9.txt"))
assert (pathfinder("dec9.txt") == 900900)
