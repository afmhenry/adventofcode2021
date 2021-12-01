#!/usr/bin/env python3
import csv


def count3PointDeeperReadings(filename):
    with open(filename, encoding="latin1") as f:
        counter = 0
        value_1 = 0
        value_2 = 0
        value_3 = 0
        curr_sum = 0
        prev_sum = 0
        for index, row in enumerate(csv.reader(f, delimiter=';')):
            current_value = int(row[0])
            value_3 = value_2
            value_2 = value_1
            value_1 = current_value
            if value_1 != 0 and value_2 != 0 and value_3 != 0:
                curr_sum = value_1 + value_2 + value_3
                if prev_sum != 0 and prev_sum < curr_sum:
                    counter += 1
                prev_sum = curr_sum

    return counter


def countDeeperReadings(filename):
    with open(filename, encoding="latin1") as f:
        counter = 0
        prev_value = 0
        for index, row in enumerate(csv.reader(f, delimiter=';')):
            current_value = int(row[0])
            if prev_value != 0 and prev_value < current_value:
                counter += 1
            prev_value = current_value
    return counter


assert (countDeeperReadings("dec1-mock.txt") == 7)
print(countDeeperReadings("dec1.txt"))


assert(count3PointDeeperReadings("dec1-2.txt") == 5)
print(count3PointDeeperReadings("dec1.txt"))
