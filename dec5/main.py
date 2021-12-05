#!/usr/bin/env python3
import csv


def findDangerIntersects(filename):
    board = [[0] * 1000 for i in range(1000)]
    points = {}
    path = []

    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=" ")):

            start = row[0].split(",")
            end = row[2].split(",")

            start_point_x = int(start[0])
            start_point_y = int(start[1])
            end_point_x = int(end[0])
            end_point_y = int(end[1])
            if start_point_x == end_point_x or start_point_y == end_point_y:
                path = valuesBetween(start_point_x, start_point_y, end_point_x, end_point_y)
                for i in range(len(path)):
                    point = path[i]
                    if str(point) not in points:
                        points[str(point)] = 1
                        board[point[1]][point[0]] = 1
                    else:
                        val = points[str(point)]
                        val_board = board[point[1]][point[0]] + 1

                        points.update({str(point): val + 1})
                        board[point[1]][point[0]] = val_board
            #else:
                #print(index, start_point_x, start_point_y, end_point_x, end_point_y)
    counter = 0
    for point in points:
        if points[point] >= 2:
            counter += 1
    return counter


def printBoardNice(board):
    print("-.-Board Start-.-")
    for row in board:
        print(row)
    print("-.-Board End-.-")


def valuesBetween(start_x, start_y, end_x, end_y):
    horiz = start_x - end_x
    vert = start_y - end_y
    points = []

    if horiz:
        for i in range(abs(horiz) + 1):
            if horiz > 0:
                points.append([start_x - i, end_y])
            else:
                points.append([start_x + i, end_y])
    elif vert:
        for i in range(abs(vert) + 1):
            if vert > 0:
                points.append([start_x, start_y - i])
            else:
                points.append([start_x, start_y + i])
    return points


assert (findDangerIntersects("dec5-mock.txt") == 5)
print(findDangerIntersects("dec5.txt"))
