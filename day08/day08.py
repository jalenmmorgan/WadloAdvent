import sys
import os
from util import parse2DArrayFile, parse1DArrayFile
from queue import PriorityQueue
import numpy as np

def run():
    os.chdir('day08')
    part1()
    part2()

def part2():
    bestViewDist = 0
    parsed = parse2DArrayFile("day08.txt", "\n", "", True)
    for row in range(len(parsed)):
        for col in range(len(parsed[row])):
            value = parsed[row][col]

            viewDist = 1
            # up
            upRow = row
            while upRow > 0:
                upRow -= 1
                if parsed[upRow][col] >= value:
                    break
            viewDist *= (row - upRow)

            # down
            downRow = row
            while downRow < len(parsed)-1:
                downRow += 1
                if parsed[downRow][col] >= value:
                    break

            viewDist *=(downRow - row)

            # left
            leftCol = col 
            while leftCol > 0:
                leftCol -= 1
                if parsed[row][leftCol] >= value:
                    break
            viewDist *=(col - leftCol)

            # right
            rightCol = col
            while rightCol < len(parsed[0])-1:
                rightCol += 1
                if parsed[row][rightCol] >= value:
                    break
            viewDist *=(rightCol - col)
            bestViewDist = max(viewDist, bestViewDist)
    print(bestViewDist)



def part1():
    parsed = parse2DArrayFile("day08.txt", "\n", "", True)

    visible = [[False for item in row] for row in parsed]
    
    for i in range(len(parsed[0])):

        # Top to bottom
        val= -1
        for rowI in range(len(parsed)):
            col = parsed[rowI][i]
            if val < col:
                val = col
                visible[rowI][i] = True

        # bottom to top
        val = -1
        for rowI in range(len(parsed)-1,-1,-1):
            col = parsed[rowI][i]
            if val < col:
                val = col
                visible[rowI][i] = True

    for rowI in range(len(parsed)):
        row = parsed[rowI]

        # left to right
        val = -1
        for i in range(len(row)):
            col = row[i]
            if val < col:
                val = col
                visible[rowI][i] = True

        # right to left
        val = -1
        for i in range(len(row)-1,-1, -1):
            col = row[i]
            if val < col:
                val = col
                visible[rowI][i] = True

    
    print(np.sum(visible))