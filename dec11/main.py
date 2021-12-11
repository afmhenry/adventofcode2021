#!/usr/bin/env python3
import csv


def octopusFlash(filename, days, second_challenge_mode):
    flashes = 0
    with open(filename, encoding="latin1") as f:
        height = len(f.readline()) - 1
        width = sum(1 for row in csv.reader(f, delimiter=" ")) + 1
        mapping = [[0 for i in range(height)] for j in range(width)]
        f.close()

    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=" ")):
            row = row.pop()
            for i, num in enumerate(row):
                mapping[index][i] = int(num)
    expanded = []

    for day in range(days):
        tickPasses(mapping)
        for i, entry in enumerate(mapping):
            for j, num in enumerate(entry):
                if num > 9 and [i, j] not in expanded:
                    expanded.append([i, j])
                    propogateFlash(i, j, mapping, expanded, height, width)
        expanded = []

        flash_this_iter = countFlashesAndReset(mapping, 0)

        if flash_this_iter == width * height and second_challenge_mode:
            return day + 1

        #print("Day:", day + 1, "Had:", flash_this_iter)
        flashes += flash_this_iter

    return flashes


def tickPasses(mapping):
    for i, entry in enumerate(mapping):
        for j, num in enumerate(entry):
            mapping[i][j] += 1


def countFlashesAndReset(mapping, flash_for_round):
    for i, entry in enumerate(mapping):
        for j, num in enumerate(entry):
            if num > 9:
                mapping[i][j] = 0
                flash_for_round += 1
    return flash_for_round


def propagateFlash(row, col, mapping, expanded, height, width):
    adjacent_positions = [
        (row, col - 1),
        (row, col + 1),
        (row + 1, col),
        (row - 1, col),
        (row - 1, col - 1),
        (row + 1, col + 1),
        (row - 1, col + 1),
        (row + 1, col - 1)
    ]
    for x, y in adjacent_positions:
        if x in range(width) and y in range(height):
            mapping[x][y] += 1
            if mapping[x][y] > 9 and [x, y] not in expanded:
                expanded.append([x, y])
                propogateFlash(x, y, mapping, expanded, height, width)
    return


def printPretty(two_dim_array):
    for row in two_dim_array:
        row_as_string = ""
        for i in range(len(row)):
            row_as_string += str(row[i])
        print(row_as_string)


assert (octopusFlash("dec11-mock.txt", 100, False) == 1656)
assert (octopusFlash("dec11.txt", 100, False) == 1591)

assert (octopusFlash("dec11-mock.txt", 1000, True) == 195)
assert (octopusFlash("dec11.txt", 1000, True) == 314)

