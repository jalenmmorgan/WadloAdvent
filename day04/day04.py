import sys
import os
from util import parse2DArrayFile
from queue import PriorityQueue
import numpy as np

def run():
    os.chdir('day04')
    parsed = parse2DArrayFile("day04.txt", "\n", ",", False)
    count = 0
    for item in parsed:
        first, second = item
        firstRange = set(range(int(first.split('-')[0]), 1+int(first.split('-')[1])))
        secondRange = set(range(int(second.split('-')[0]), 1+int(second.split('-')[1])))
        combinedSize = len(firstRange.union(secondRange))
        if combinedSize < len(secondRange)+ len(firstRange):
            count+= 1

    print(count)