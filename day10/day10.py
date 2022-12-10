import sys
import os
from util import parse2DArrayFile, parse1DArrayFile
from queue import PriorityQueue
import numpy as np

def run():
    os.chdir('day10')
    parsed = parse2DArrayFile("day10.txt", "\n", "")
    print(parsed)