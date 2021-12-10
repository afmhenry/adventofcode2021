#!/usr/bin/env python3
import csv
import math
import pandas as pd
import copy
from threading import Thread

key_keeper = ["(", "[", "{", "<"]
lock_keeper = [")", "]", "}", ">"]
book_keeper = [3, 57, 1197, 25137]


def corruptionHammer(filename):
    with open(filename, encoding="latin1") as f:
        score_total = 0
        weird_scores = []
        for index, row in enumerate(csv.reader(f, delimiter=" ")):
            row = row.pop()
            score = 0
            score = findBreak(row)
            print(index,score)
            score_total += score
            if score == 0:
                score_new = calcNerdScore(fixIncomplete(row))
                print(score_new)
                weird_scores.append(score_new)
        weird_scores.sort()
        return weird_scores[(round(len(weird_scores)/2))-1]


def findBreak(row):
    active_chunks = []
    for char in row:
        if char in key_keeper:
            active_chunks.append(char)
        else:
            if lock_keeper.index(char) != key_keeper.index(active_chunks.pop()):
                return book_keeper[lock_keeper.index(char)]
    return 0


def fixIncomplete(row):
    active_chunks = []
    repaired_chunks = []
    for char in row:
        if char in key_keeper:
            active_chunks.append(char)
        else:
            active_chunks.pop()

    for char in active_chunks:
        repaired_chunks.append(lock_keeper[key_keeper.index(char)])

    repaired_chunks.reverse()
    return repaired_chunks


def calcNerdScore(chunk_fixes):
    score = 0
    for char in chunk_fixes:
        score *= 5
        score += (lock_keeper.index(char)+1)
    return score

print (corruptionHammer("dec10-mock.txt"))
print(corruptionHammer("dec10.txt"))
# assert (corruptionHammer("dec10-mock.txt") == 1134)

# print(corruptionHammer("dec10.txt"))
# assert (corruptionHammer("dec10.txt") == 900900)
