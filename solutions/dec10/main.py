#!/usr/bin/env python3
import csv
import math
import pandas as pd
import copy
from threading import Thread

key_keeper = ["(", "[", "{", "<"]
lock_keeper = [")", "]", "}", ">"]
book_keeper = [3, 57, 1197, 25137]


def corruptionHammer(filename, second_mode):
    with open(filename, encoding="latin1") as f:
        score_total = 0
        weird_scores = []
        for index, row in enumerate(csv.reader(f, delimiter=" ")):
            row = row.pop()
            score = 0
            score = findBreak(row)
            score_total += score
            if score == 0:
                score_new = calcNerdScore(fixIncomplete(row))
                weird_scores.append(score_new)
        weird_scores.sort()

        return weird_scores[(math.floor(len(weird_scores) / 2))] if second_mode else score_total


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
        score += (lock_keeper.index(char) + 1)
    return score


assert(corruptionHammer("dec10-mock.txt", False) == 26397)
assert(corruptionHammer("dec10.txt", False) == 345441)

assert(corruptionHammer("dec10-mock.txt", True) == 288957)
assert(corruptionHammer("dec10.txt", True) == 3235371166)
