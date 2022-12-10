import sys
import os
from util import parse2DArrayFile, parse1DArrayFile
from queue import PriorityQueue
import numpy as np

def run():
    os.chdir('day15')
    parsed = parse2DArrayFile("day15.txt", "\n", "")
    print(parsed)