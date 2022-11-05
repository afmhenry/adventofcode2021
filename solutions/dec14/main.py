#!/usr/bin/env python3
import csv

queue = []


def evaluatePairs(filename, steps, second_challenge_mode):
    original_base = ""
    evaluated_base_on_step = []
    translations = []
    possible_chars = set()

    with open(filename, encoding="latin1") as f:
        for index, row in enumerate(csv.reader(f, delimiter=" ")):
            if index == 0:
                original_base = row.pop()
            elif row:
                translations.append((row[0], row[2]))
                possible_chars.add(row[0][0])
                possible_chars.add(row[0][1])
                possible_chars.add(row[2])
        f.close()
    print(original_base, translations)

    if not second_challenge_mode:
        for step in range(steps+1):
            print(step)
            if step == 0:
                evaluated_base_on_step.append(original_base)
            else:
                evaluated_base_on_step.append(replacedPairsSlow(evaluated_base_on_step[step-1], translations))
    else:
        new_translations = moreTranslations(translations)
        translations = new_translations + translations
        for step in range(steps+1):
            print("step",step)
            if step == 0:
                evaluated_base_on_step.append(original_base)
            else:
                evaluated_base_on_step.append(replacedPairsFAST(evaluated_base_on_step[step-1], translations))
                print(evaluated_base_on_step)
    last_eval = evaluated_base_on_step.pop()

    maximum = 0
    minimum = 0
    for pos_char in possible_chars:
        count_of_char = last_eval.count(pos_char)
        maximum = count_of_char if count_of_char > maximum else maximum
        minimum = count_of_char if count_of_char < minimum or minimum == 0 else minimum

    return maximum-minimum


def moreTranslations(translations):
    new_translations = []
    for option in translations:
        print(option[0][0] + option[1] + option[0][1])
        result = replacedPairsSlow(option[0][0] + option[1] + option[0][1], translations)
        new_translations.append((option[0][0] + option[1] + option[0][1],result))

    return new_translations


def replacedPairsSlow(base, translations):
    new_base = ""
    for i, element in enumerate(base):
        if i == 0:
            new_base += base[i]
        if i+1 < len(base):
            for option in translations:
                if option[0] == base[i]+base[i+1]:
                    #print(base[i], option[1], base[i+1])
                    new_base += option[1] + base[i+1]
    return new_base


def replacedPairsFAST(base, translations):
    new_base = ""
    for i, element in enumerate(base):
        print(element)
        if i == 0:
            new_base += base[i]
        for option in translations:
            #print(len(option[0]),i,len(base))
            if (i + len(option[0])+1) <= len(base):
                #print(option[0])
                next_entries = ""
                for k in range(len(option[0])-1):
                    next_entries += base[k+i]
                #print("next",new_base+next_entries, i, option)
                if new_base + next_entries == option[0]:
                    print(new_base)
                    new_base += option[1] + next_entries
                    print("post",new_base)
                    #print("match", option, next_entries, new_base)
                    continue
    print("return")
    return new_base


#assert(evaluatePairs("dec16-mock.txt", 10, False) == 1588)
print(evaluatePairs("dec14-mock.txt", 1, True))


#print(evaluatePairs("dec16-mock.txt", 40, False))

# print (findPath("dec15.txt", False) == 1591)

# print (findPath("dec15-mock.txt", True) == 195)
# print (findPath("dec15.txt", True) == 314)
