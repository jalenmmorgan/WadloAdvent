import sys
import os
from util import parse2DArrayFile
from queue import PriorityQueue
import numpy as np

def run():
    os.chdir('day03')
    parsed = parse2DArrayFile("day03.txt", "\n", "")
    print(parsed)

    total = 0
    while len(parsed) > 0:
        first = parsed.pop(0)
        second = parsed.pop(0)
        third = parsed.pop(0)

        ordVal = ord(list(set(first).intersection(set(second)).intersection(set(third)))[0])
        if ordVal > 90: # lowercase
            ordVal -= 96
        else:
            ordVal -= 38

        total += ordVal

    print(total)
