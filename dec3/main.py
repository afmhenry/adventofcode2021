#!/usr/bin/env python3
import csv

def measureLifeSupport(filename):
    width = 0
    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=' ')):
            byte = list(row[0])
            width = len(byte)

    prev_o2 = []
    prev_co2 = []
    o2_row = ""
    co2_row = ""
    for i in range(width):
        column = ""
        with open(filename, encoding="latin1") as f:
            for index, row in enumerate(csv.reader(f, delimiter=' ')):
                byte = list(row[0])
                column += byte[i]

        indexes_of_0 = [k for k, j in enumerate(column) if j == "0"]
        indexes_of_1 = [kk for kk, jj in enumerate(column) if jj == "1"]
        co2_accept_rows = []
        o2_accept_rows = []

        if i > 0:
            indexes_of_0_o = [x for x in indexes_of_0 if x in prev_o2]
            indexes_of_0_c = [x for x in indexes_of_0 if x in prev_co2]
            indexes_of_1_o = [x for x in indexes_of_1 if x in prev_o2]
            indexes_of_1_c = [x for x in indexes_of_1 if x in prev_co2]
        else:
            indexes_of_0_o = indexes_of_0
            indexes_of_0_c = indexes_of_0
            indexes_of_1_o = indexes_of_1
            indexes_of_1_c = indexes_of_1

        if len(indexes_of_1_o) >= len(indexes_of_0_o):
            o2_accept_rows = indexes_of_1_o
        else:
            o2_accept_rows = indexes_of_0_o

        if len(indexes_of_1_c) >= len(indexes_of_0_c):
            co2_accept_rows = indexes_of_0_c
        else:
            co2_accept_rows = indexes_of_1_c

        if i > 0:
            prev_o2 = set(prev_o2).intersection(set(o2_accept_rows))
            prev_co2 = set(prev_co2).intersection(set(co2_accept_rows))
        else:
            prev_o2 = o2_accept_rows
            prev_co2 = co2_accept_rows

        if len(prev_o2) == 1:
            o2_row = prev_o2.pop()
        if len(prev_co2) == 1:
            co2_row = prev_co2.pop()

    co2_value = ""
    o2_value = ""
    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=' ')):
            if index == int(co2_row):
                co2_value = int(row[0], 2)
            if index == int(o2_row):
                o2_value = int(row[0], 2)

    return co2_value*o2_value


def measurePower(filename):
    with open(filename, encoding="latin1") as f:
        counter = []
        gamma = ""
        epsilon = ""
        for index, row in enumerate(csv.reader(f, delimiter=' ')):
            byte = list(row[0])

            for i in range(len(byte)):

                if not len(counter) > i:
                    counter.insert(i, {
                        "0": 0,
                        "1": 0
                    })
                counter[i][byte[i]] += 1

        for column in counter:
            if column["0"] > column["1"]:
                gamma += "0"
                epsilon += "1"
            else:
                gamma += "1"
                epsilon += "0"
        return int(gamma, 2) * int(epsilon, 2)


assert(measurePower("dec3-mock.txt") == int("198", 10))
print(measurePower("dec3.txt"))

assert(measureLifeSupport("dec3-mock.txt") == int("230", 10))
print(measureLifeSupport("dec3.txt"))


# assert(countPositionWithAim("dec2-mock.txt") == 900)
# print(countPositionWithAim("dec2.txt"))
