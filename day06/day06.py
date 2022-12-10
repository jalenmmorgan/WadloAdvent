import sys
import os
from util import parse1DArrayFile
from queue import PriorityQueue
import numpy as np

def run():
    os.chdir('day06')
    parsed = parse1DArrayFile("day06.txt", "\n")[0]
    for i in range(len(parsed)):
        selection = parsed[i:i+14]
        if len(set(selection)) == 14:
            print(i+14)
            return
    print(parsed)