#!/usr/bin/env python3
import csv
from threading import Thread


def countFish(filename, days):
    fishies = []
    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=",")):
            fishies = list(row)
            fishies = [int(x) for x in fishies]
            return explode(fishies, days)


def countFishOptimized(filename, days):
    fishies_optimized = [0 for i in range(9)]
    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=",")):
            fishies = list(row)
            fishies = [int(x) for x in fishies]
            list.sort(fishies)
            for i in range(len(fishies)):
                fishies_optimized[fishies[i]] += 1
    return explodeOptimized(fishies_optimized, days)


def explodeOptimized(fishies, days):
    shifted_fishies = []
    shifted_fishies = [0 for k in range(9)]

    for day in range(days):
        for i in range(len(fishies)):
            if i == 0:
                shifted_fishies[8] = fishies[i]
                shifted_fishies[6] = fishies[i]
            elif 0 < i < 7:
                shifted_fishies[i - 1] = fishies[i]
            else:
                shifted_fishies[i - 1] += fishies[i]

        fishies = shifted_fishies
        shifted_fishies = [0 for k in range(9)]

    return sum(fishies)


def explode(fishies, days):
    for day in range(days):
        new_fishies = []
        for i in range(len(fishies)):
            fish_days = fishies[i] - 1
            if fish_days < 0:
                new_fishies.append(8)
                fishies[i] = 6
            else:
                fishies[i] = fish_days
        fishies += new_fishies
    return len(fishies)


assert (countFish("dec6-mock.txt", 18) == 26)
print(countFish("dec6.txt", 80))  # 388739
assert (countFishOptimized("dec6-mock.txt", 18) == 26)
assert (countFishOptimized("dec6.txt", 80) == 388739)
assert (countFishOptimized("dec6-mock.txt", 256) == 26984457539)
print(countFishOptimized("dec6.txt", 256))  # 1741362314973
