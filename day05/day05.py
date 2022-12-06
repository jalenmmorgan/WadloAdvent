import sys
import os
from util import parse2DArrayFile, parseAllNumbersFromSentences
from queue import PriorityQueue
import numpy as np

def run():
    os.chdir('day05')

    crates = [['B','W','N'], 
    ['L','Z','S','P','T','D','M','B'],
    ['Q','H','Z','W','R'],
    ['W','D','V','J','Z','R'],
    ['S','H','M','B'],
    ['L','G','N','J','H','V','P','B'],
    ['J','Q','Z','F','H','D','L','S'],
    ['W','S','F','J','G','Q','B'],
    ['Z','W','M','S','C','D','J']]

    l = parseAllNumbersFromSentences("day05.txt")
    for instruction in l:
        """
        for r in range(instruction[0]):
            item = crates[instruction[1]-1].pop()
            crates[instruction[2]-1].append(item)
    
        """
        items = crates[instruction[1]-1][-instruction[0]::]
        del crates[instruction[1]-1][-instruction[0]::]
        crates[instruction[2]-1].extend(items)
    print(str(''.join([item[-1] for item in crates])))
