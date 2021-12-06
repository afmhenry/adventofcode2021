#!/usr/bin/env python3
import csv
from threading import Thread


def countFish(filename, days):
    fishies = []

    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=",")):
            fishies = list(row)
            fishies = [int(x) for x in fishies]
            explode(fishies,days)


def explode(fishies, days):
    days_unchanged = days
    new_fishies = []
    for day in range(days):
        print(day)

        for i in range(len(fishies)):
            fish_days = fishies[i] - 1
            if fish_days < 0:
                new_fishies.append(8)
                fishies[i] = 6
            else:
                fishies[i] = fish_days
        fishies += new_fishies
    return len(fishies)


assert (countFish("dec6-mock.txt", 80) == 5934)
print(countFish("dec6.txt", 80))
