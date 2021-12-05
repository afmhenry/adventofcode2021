#!/usr/bin/env python3
import csv


def findDangerIntersects(filename, support_diagonal, print_board):
    board_size = 1000
    if print_board:
        board_size = 10

    board = [[0] * board_size for i in range(board_size)]
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

            if start_point_x == end_point_x or start_point_y == end_point_y or support_diagonal:
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
                #print("Skip", index)
                # print(index, start_point_x, start_point_y, end_point_x, end_point_y)
    counter = 0
    for point in points:
        if points[point] >= 2:
            counter += 1
    if print_board:
        printBoardNice(board)
    return counter


def printBoardNice(board):
    print("-.-Board Start-.-")
    for row in board:
        print(row)
    print("-.-Board End-.-")


def valuesBetween(start_x, start_y, end_x, end_y):

    horiz = start_x - end_x
    if horiz < 0:
        j = 1
    else:
        j = -1

    vert = start_y - end_y
    if vert < 0:
        k = 1
    else:
        k = -1
    points = []

    if horiz and vert and (abs(horiz) == abs(vert)):
        horiz -= j
        vert -= k
        while horiz != 0 and vert != 0:
            horiz += j
            vert += k
            points.append(
                [
                    end_x + horiz,
                    end_y + vert
                ]
            )
    elif horiz:
        horiz -= j
        while horiz != 0:
            horiz += j
            points.append(
                [
                    end_x + horiz,
                    end_y
                ]
            )
    elif vert:
        vert -= k
        while vert != 0:
            vert += k
            points.append(
                [
                    start_x,
                    end_y + vert
                ]
            )

    return points


assert(findDangerIntersects("dec5-mock.txt", False, True) == 5)
print(findDangerIntersects("dec5.txt", False, False))

assert (findDangerIntersects("dec5-mock.txt", True, True) == 12)
print(findDangerIntersects("dec5.txt", True, False))
