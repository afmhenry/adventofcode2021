#!/usr/bin/env python3
import csv
import math
from threading import Thread


def signals(filename, second_mode):
    count = 0
    with open(filename, encoding="latin1") as f:
        zero = [["z" * 6], ["z" * 6]]
        one = [["z" * 2], ["z" * 2]]
        two = [["z" * 5], ["z" * 5]]
        five = [["z" * 5], ["z" * 5]]
        three = [["z" * 5], ["z" * 5]]
        four = [["z" * 6], ["z" * 6]]
        six = [["z" * 6], ["z" * 6]]
        nine = [["z" * 6], ["z" * 6]]
        seven = [["z" * 3], ["z" * 3]]
        eight = [["z" * 7], ["z" * 7]]

        total = 0

        for index, row in enumerate(csv.reader(f, delimiter="|")):
            multiplier = 0
            total += findEasy(row[1].split(" "), one, four, seven, eight)
            findEasy(row[0].split(" "), one, four, seven, eight)

            parsed_row = row[0].split(" ") + row[1].split(" ")
            for i, number in enumerate(parsed_row):
                num = len(number)
                number = sorted(number)
                if num == 6:
                    if set(one[0]).issubset(set(number)):
                        if set(four[0]).issubset(set(number)):
                            nine[0] = number
                            nine[1] = ["a", "b", "c", "d", "f", "g"]
                        else:
                            zero[0] = number
                            zero[1] = ["a", "b", "c", "e", "f", "g"]
                    else:
                        six[0] = number
                        six[1] = ["a", "b", "d", "e", "f", "g"]

            for i, number in enumerate(parsed_row):
                num = len(number)
                number = sorted(number)
                if num == 5:
                    if set(one[0]).issubset(number):
                        three[0] = number
                        three[1] = ["a", "c", "d", "f", "g"]
                    else:
                        if len(list(dict.fromkeys(nine[0] + number))) == (len(number) + 1):
                            five[0] = number
                            five[1] = ["a", "b", "d", "f", "g"]
                        else:
                            two[0] = number
                            two[1] = ["a", "c", "d", "e", "g"]

            string_count = ""
            for entry in row[1].split(" "):
                if entry:
                    if sorted(entry) == zero[0]:
                        string_count += "0"
                    elif sorted(entry) == one[0]:
                        string_count += "1"
                    elif sorted(entry) == two[0]:
                        string_count += "2"
                    elif sorted(entry) == three[0]:
                        string_count += "3"
                    elif sorted(entry) == four[0]:
                        string_count += "4"
                    elif sorted(entry) == five[0]:
                        string_count += "5"
                    elif sorted(entry) == six[0]:
                        string_count += "6"
                    elif sorted(entry) == seven[0]:
                        string_count += "7"
                    elif sorted(entry) == eight[0]:
                        string_count += "8"
                    elif sorted(entry) == nine[0]:
                        string_count += "9"
            count += int(string_count)
    return count if second_mode else total


def findEasy(row, one, four, seven, eight):
    one_four_seven_or_eight = 0
    for i, number in enumerate(row):
        num = len(number)
        number = sorted(number)

        if num == 2:
            one[0] = number
            one[1] = ["c", "f"]
            one_four_seven_or_eight += 1
        elif num == 4:
            four[0] = number
            four[1] = ["b", "c", "d", "f"]
            one_four_seven_or_eight += 1
        elif num == 3:
            seven[0] = number
            seven[1] = ["a", "c", "f"]
            one_four_seven_or_eight += 1
        elif num == 7:
            eight[0] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            eight[1] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            one_four_seven_or_eight += 1
    return one_four_seven_or_eight

assert(signals("dec8-mock.txt", False) == 26)
assert(signals("dec8.txt", False) == 239)

assert(signals("dec8-mock.txt", True) == 61229)
assert(signals("dec8.txt", True) == 946346)
