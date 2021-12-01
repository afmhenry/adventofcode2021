#!/usr/bin/env python3
import sys
import re

import csv


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
print( countDeeperReadings("dec1.txt") )
