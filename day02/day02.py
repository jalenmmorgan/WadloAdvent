import sys
import os
from util import parse2DArrayFile, parseSingleCharacter2DArray, parseLineThenSpace
from queue import PriorityQueue
import numpy as np

def run():
    os.chdir('day02')
    parsed = parseLineThenSpace("day02.txt")
    print(parsed)

    score = 0
    for item in parsed:

        item[1] = getStrategy(item[0], item[1])
        score += getScore(item[0], item[1])
        print(score)
        if item[1] == "X":
            score += 1
        if item[1] == "Y":
            score += 2
        if item[1] == "Z":
            score += 3

    print()
    print(score)
    print(getScore("A","Y"))

def getStrategy(item1, item2):
    if item2 == "X":
        if item1 == "A":
            return "Z"
        if item1 == "B":
            return "X"
        if item1 == "C":
            return "Y"
    if item2 == "Y":
        if item1 == "A":
            return "X"
        if item1 == "B":
            return "Y"
        if item1 == "C":
            return "Z"
    if item2 == "Z":
        if item1 == "A":
            return "Y"
        if item1 == "B":
            return "Z"
        if item1 == "C":
            return "X"
           
def getScore(item1, item2):
    value = (ord(item1) - ord(item2)) % 3

    match value:
        case 0:
            return 6
        case 1:
            return 3
        case 2:
            return 0