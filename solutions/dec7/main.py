#!/usr/bin/env python3
import csv
import math
from threading import Thread


def crabArmy(filename, second_mode):
    crabs = []
    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=",")):
            crabs = list(row)
            crabs = [int(x) for x in crabs]
            crabs.sort()
            length = crabs[int(len(crabs) - 1)] + 1
            crabs_positioned = [0 for i in range(length)]
            for pos in range(len(crabs)):
                crabs_positioned[crabs[pos]] += 1
            # potential_solutions = binarySort(crabs_positioned, [0, length-1])
            prev_cost = 0
            least_fuel = 1111111111111110
            for solution in range(len(crabs_positioned)):
                cost = 0
                for i in range(length):
                    if crabs_positioned[i]:
                        diff = abs(solution - i)
                        if second_mode:
                            cost += abs((diff * (diff + 1) / 2) * crabs_positioned[i])
                        else:
                            cost += abs(diff * crabs_positioned[i])
                if cost < least_fuel:
                    least_fuel = cost

            return cost if cost < least_fuel else least_fuel


def binarySort(crabs_positioned, range_of_returned):
    halfway = int(math.floor(len(crabs_positioned) / 2))
    end = int(len(crabs_positioned))
    starting_index = range_of_returned[0]
    ending_index = range_of_returned[1]
    print(starting_index, ending_index, halfway)
    h1 = 0
    h2 = 0
    h1_list = []
    h2_list = []

    for first in range(0, halfway):
        h1 += crabs_positioned[first]
        h1_list.append(crabs_positioned[first])
    for second in range(halfway, end):
        h2 += crabs_positioned[second]
        h2_list.append(crabs_positioned[second])
    range_of_returned = [starting_index, ending_index - halfway] if h1 > h2 else [ending_index - halfway, ending_index]
    print("h1", h1, " h2", h2, " range", range_of_returned)

    if halfway > 2:
        return binarySort(h1_list if h1 > h2 else h2_list, range_of_returned)
    else:
        return range_of_returned


assert(crabArmy("dec7-mock.txt", False) == 37)
assert(crabArmy("dec7.txt", False) == 356958)

assert(crabArmy("dec7-mock.txt", True) == 168)
assert(crabArmy("dec7.txt", True) == 105461913)
