import sys
import os
from util import parse2DArrayFile, parse1DArrayFile
from queue import PriorityQueue
import numpy as np


allSmallEnoughSizes = []

class Tree:
    def __init__(self, name):
        self.parent = None
        self.folderChildren = []
        self.fileChildren = {}
        self.name = name
        self.directorySize = 0

    def addChildFolder(self, childTree):
        if not childTree in self.folderChildren:
            self.folderChildren.append(childTree)
            childTree.parent = self

    def addChildFile(self, childFileName, size):
        if not childFileName in self.fileChildren.keys():
            self.fileChildren[childFileName] = int(size)

    def __str__(self):
        return self.name + "\n" + str(self.fileChildren.keys()) + "\n" + str(self.folderChildren)
    
    def refreshDirectorySize(self):
        size = 0
        for item in self.folderChildren:
            size += item.refreshDirectorySize()
        for item in self.fileChildren.keys():
            size += self.fileChildren[item]
        self.directorySize = size
        if size < 100000:
            print(size)
            allSmallEnoughSizes.append(size)
        return size

    def getSmallestDirectoryAbove(self, value):
        smallest = 99999999999999999999999
        for item in self.folderChildren:
            smallest= min(smallest, item.getSmallestDirectoryAbove(value))
        if self.directorySize >= value:
            smallest = min(self.directorySize, smallest)
        return smallest

def run():
    os.chdir('day07')
    parsed = parse1DArrayFile("day07.txt", "\n")

    tree = Tree('/')
    tree.parent = tree
    place = tree

    for item in parsed[1:]:

        if item[0] == "$":
            if item[2:4] == "cd":
                if item[5:7] == '..':
                    place = place.parent
                elif item[5:] == '/':
                    place = tree
                else:
                    newDirectory = item[5:]
                    for item in place.folderChildren:
                        if item.name == newDirectory:
                            place = item
                            break
            elif item[2:4] == "ls":
                True
        elif item[0:3] == "dir":
            directoryName = item[4:]
            found = False
            for thing in place.folderChildren:
                if thing.name == directoryName:
                    found= True
            if not found:
                place.addChildFolder(Tree(directoryName))

        else: #file size
            size, filename = item.split(" ")
            place.addChildFile(filename, size)
    tree.refreshDirectorySize()

    spaceNeededToBeFree = tree.directorySize - (70000000 - 30000000)
    print("ansnwer: " + str(tree.getSmallestDirectoryAbove(spaceNeededToBeFree)))

