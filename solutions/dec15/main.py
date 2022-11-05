#!/usr/bin/env python3
import csv


def findPath(filename, days, second_challenge_mode):
    flashes = 0
    with open(filename, encoding="latin1") as f:
        height = len(f.readline()) - 1
        width = sum(1 for row in csv.reader(f, delimiter=" ")) + 1
        mapping = [[0 for i in range(height)] for j in range(width)]
        f.close()

    # print(cheapest_path_to.get((0,0))) = (1, [(0, 0), (0, 0)])
    # print(cheapest_path_to.get((0,0))[0]) = 1 sum
    # print(cheapest_path_to.get((0,0))[1]) = [(0, 0), (0, 0)]
    # print(cheapest_path_to.get((0,0))[1][0]) = (0, 0)

    cheapest_path_to = {
        (0, 0):
            (1, [(0, 0), (0, 0)])
    }
    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=" ")):
            row = row.pop()
            for i, num in enumerate(row):
                mapping[index][i] = int(num)
        printPretty(mapping)

        for i in range(height):

            for j in range(i + 1):
                print(i, j)
                print(i, j)

                findToPoint(j, i, cheapest_path_to, height)
                if (i, j) != (j, i):
                    findToPoint(i, j, cheapest_path_to, height)

        f.close()

    return flashes


def findToPoint(col, row, cheapest_path_to, height):
    path = []
    adjacent_positions = [
        (col, row - 1),
        (col, row + 1),
        (col + 1, row),
        (col - 1, row)
    ]
    cost = 0
    limit = col if col > row else row

    for col, row in adjacent_positions:
        if col in range(height) and \
           row in range(height):
            return



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
                propagateFlash(x, y, mapping, expanded, height, width)
    return


def printPretty(two_dim_array):
    for row in two_dim_array:
        row_as_string = ""
        for i in range(len(row)):
            row_as_string += str(row[i])
        print(row_as_string)


print(findPath("dec15-mock.txt", 100, False))
