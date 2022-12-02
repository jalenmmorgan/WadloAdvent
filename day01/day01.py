import sys
import os
from util import parse2DArrayFile
from queue import PriorityQueue

def run():
    os.chdir('day01')

    que = PriorityQueue()
    parsed = parse2DArrayFile("day01.txt")
    for item in parsed:
        summed = sum(item)
        que.put(summed)
        if que.qsize() > 3:
            que.get()

    summed = 0
    while que.qsize() > 0:
        summed += que.get()

    print(summed)        
