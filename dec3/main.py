#!/usr/bin/env python3
import csv



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

# assert(countPositionWithAim("dec2-mock.txt") == 900)
# print(countPositionWithAim("dec2.txt"))
