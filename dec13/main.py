#!/usr/bin/env python3
import csv

queue = []


def foldPaper(filename, second_challenge_mode):
    dots = [[]]
    max_x = 0
    max_y = 0
    instructions = []

    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=",")):

            if row and len(row) != 2:
                print("instructions")
                row = row.pop()
                instructions.append((row.split("=")[0].split(" ")[2], int(row.split("=")[1])))
                print(instructions)
            elif row:
                if int(row[1]) > max_y:
                    max_y = int(row[1])
                if int(row[0]) > max_x:
                    max_x = int(row[0])
        f.close()

    height = max_y+1
    width = max_x+1

    dots = [["." for i in range(width)] for j in range(height)]

    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=",")):

            if row != "" and len(row) == 2:
                dots[int(row[1])][int(row[0])] = "#"

        f.close()


    #printPretty(dots)

    for instruction in instructions:
        #print(instruction)
        dots, height, width = transpose(instruction, dots, width, height)
    printPretty(dots)

    dot_count = 0

    for row in dots:
        for dot in row:
            if dot == "#":
                dot_count += 1
    return dot_count

def transpose(instruction, dots, width, height):
    new_dots = [[]]
    if instruction[0] == "y":
        #print("horiz",instruction[1],width)
        new_dots = [["." for i in range(width)] for j in range(instruction[1])]
        for i, row in enumerate(dots):
            #print("i",i)
            for j, col in enumerate(row):
                #print("ij",i,j)
                if i == (instruction[1]):
                    #print("cont",col)
                    continue
                if i > (instruction[1]):
                    i = instruction[1]- (i - instruction[1])
                    #print("after caclc",i,j, col)
                if new_dots[i][j] == ".":
                    new_dots[i][j] = col
        height = instruction[1]
        #print("h",height)
    elif instruction[0] == "x":
        #print("vert", instruction[1], height)
        new_dots = [["." for i in range(instruction[1])] for j in range(height)]
        for i, row in enumerate(dots):
            #print("i",i)
            for j, col in enumerate(row):
                #print("ij", i, j)
                if j == (instruction[1]):
                    #print("cont", col)
                    continue
                if j > (instruction[1]):
                    j = instruction[1] - (j - instruction[1])
                    #print("after caclc", i, j, col)
                if new_dots[i][j] == ".":
                    new_dots[i][j] = col
        width = instruction[1]
        #print("w",width)
    return new_dots, height, width


def printPretty(two_dim_array):
    for row in two_dim_array:
        row_as_string = ""
        for i in range(len(row)):
            row_as_string += str(row[i])
        print(row_as_string)


assert(foldPaper("dec13-mock.txt", False) == 16)
print(foldPaper("dec13.txt", False))
# print (findPath("dec15.txt", False) == 1591)

# print (findPath("dec15-mock.txt", True) == 195)
# print (findPath("dec15.txt", True) == 314)
