#!/usr/bin/env python3
import csv

queue = []


def bitDecode(filename, steps, second_challenge_mode):
    original_base = ""
    evaluated_base_on_step = []
    translations = []
    possible_chars = set()

    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=" ")):




print(bitDecode("dec16-mock.txt", 1, False))
