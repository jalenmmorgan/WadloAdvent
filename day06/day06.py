import sys
import os
from util import parse2DArrayFile
from queue import PriorityQueue
import numpy as np

def run():
    os.chdir('day06')
    parsed = parse2DArrayFile("day06.txt", "\n", "")
    print(parsed)