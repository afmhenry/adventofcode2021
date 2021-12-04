#!/usr/bin/env python3
import csv


def bingoWinner(filename):
    boards = []
    board = [[-1] * 5 for i in range(5)]

    moves = ""
    i = 0

    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f)):
            if index == 0:
                moves = row
                k = 0
            elif row:
                for j, value in enumerate(str.split(row[0])):
                    board[k][j] = int(value)
                k += 1
                if k == 4:
                    boards.append(board)
            else:
                k = 0
                board = [[-1] * 5 for i in range(5)]

    for move in moves:
        for i, board in enumerate(boards):
            for j,  rows in enumerate(board):
                for k,  cell in enumerate(rows):
                    if cell == int(move):
                        boards[i][j][k] = -1
                        if sum(boards[i][j]) == -5:
                            return int(move) * getSumOfBoard(boards[i])
                        else:
                            column = []
                            for jj, rows_2 in enumerate(board):
                                column.append(rows_2[k])
                            if sum(column) == -5:
                                return int(move) * getSumOfBoard(boards[i])


def getSumOfBoard(board):
    sum = 0
    for j, rows in enumerate(board):
        for k, cell in enumerate(rows):
            if cell >= 0:
                sum += cell
    return sum


    return "foo"


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


assert(bingoWinner("dec4-mock.txt") == 4512)
print(bingoWinner("dec4.txt"))

