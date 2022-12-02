import requests as re


def downloadFile(url, filepath):
    response = re.get(url)
    print(response.status_code)
    print(response.content)

# Parses a text file into a 2D array.
def parse2DArrayFile(fileName, rowSeparator, colSeparator, makeNumbers = False):
    f = open(fileName, "r")
    text = f.read()
    rows = text.split(rowSeparator)
    if (colSeparator) != "":
        withCols = [item.split(colSeparator) for item in rows]
    else:
        withCols = [[*item] for item in rows]

    if makeNumbers:  
        return [[stringToNumber(col) for col in row] for row in withCols]
    else:
        return withCols

def parse2DArrayDoubleNewLine(fileName, makeNumbers=False):
    return parse2DArrayFile(fileName, "\n\n", "\n", makeNumbers)

def parseSingleCharacter2DArray(fileName, makeNumbers=False):
    return parse2DArrayFile(fileName, "\n", "", makeNumbers)

def parseLineThenSpace(fileName, makeNumbers=False):
    return parse2DArrayFile(fileName, "\n", " ", makeNumbers)

def stringToNumber(item):
    if item == "":
        return 0
    return int(item)
