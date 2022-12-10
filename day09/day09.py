import sys
import os
from util import parse2DArrayFile, parse1DArrayFile
from queue import PriorityQueue
import numpy as np

def run():
    os.chdir('day09')
    parsed = parse2DArrayFile("day09.txt", "\n", " ")
    numRows = 1000
    numCols = 1000
    visitedGrid = [[False for i in range(numCols)] for j in range(numRows)]
    headPosition = [numRows//2, numCols//2]
    tailPositions = [[numRows//2, numCols//2] for i in range(9)]

    def displayGrid(headPosition, tailPosition, visitedGrid):
        displaySize = 5
        for row in range(numRows//2-displaySize, numRows//2+displaySize):
            print("\n")
            for col in range(numCols//2-displaySize, numCols//2+displaySize):
                if row == headPosition[0] and col == headPosition[1]:
                    print(" H ", end="")
                elif row == tailPosition[0] and col == tailPosition[1]:
                    print(" T ", end="")
                else:
                    print(" . ", end="")
        print("\n\n")


    visitedGrid[tailPositions[-1][0]][ tailPositions[-1][1]] = True

    for i in range(len(parsed)):
        item = parsed[i]
        print(item)
        if item[0] == "L":
            for i in range(int(item[1])):
                headPosition[0] -= 1
                tailPositions = updateAllPositions(headPosition, tailPositions)
                visitedGrid[tailPositions[-1][0]][ tailPositions[-1][1]] = True


        if item[0] == "R":
            for i in range(int(item[1])):
                headPosition[0] += 1
                tailPositions = updateAllPositions(headPosition, tailPositions)
                visitedGrid[tailPositions[-1][0]][ tailPositions[-1][1]] = True

        if item[0] == "U":
            for i in range(int(item[1])):
                headPosition[1] -= 1
                tailPositions = updateAllPositions(headPosition, tailPositions)
                visitedGrid[tailPositions[-1][0]][ tailPositions[-1][1]] = True

        if item[0] == "D":
            for i in range(int(item[1])):
                headPosition[1] += 1
                tailPositions = updateAllPositions(headPosition, tailPositions)
                visitedGrid[tailPositions[-1][0]][ tailPositions[-1][1]] = True
        displayGrid(headPosition, tailPositions[-1], 0)
    print(np.sum(visitedGrid))


def updateAllPositions(headPosition, tailPositions):
    currThingToFollow = headPosition
    for i in range(len(tailPositions)):
        tailPositions[i] = updatePosition(tailPositions[i], currThingToFollow)
        currThingToFollow = tailPositions[i]
    return tailPositions

def updatePosition(tailPosition, headPosition):
    if headPosition[0] == tailPosition[0] and headPosition[1] == tailPosition[1]:
        print("case 1")
        return tailPosition
    elif headPosition[0] == tailPosition[0]:
        print("case 2")
        tailPosition[1] = headPosition[1]+np.sign(tailPosition[1]-headPosition[1])
    elif headPosition[1] == tailPosition[1]:
        print("case 3")
        tailPosition[0] = headPosition[0]+np.sign(tailPosition[0] - headPosition[0])
    else:
        print("case 4")
        xDirection = np.sign(headPosition[0]-tailPosition[0])
        yDirection = np.sign(headPosition[1] - tailPosition[1])
        dist = max(abs(headPosition[0]-tailPosition[0]), abs(headPosition[1]-tailPosition[1]))
        if dist > 1:
            tailPosition[0] += xDirection
            tailPosition[1] += yDirection
    return tailPosition