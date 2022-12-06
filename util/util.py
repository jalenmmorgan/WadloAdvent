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

def parse1DArrayFile(fileName, rowSeparator, makeNumbers = False):
    f = open(fileName, "r")
    text = f.read()
    rows = text.split(rowSeparator)

    if makeNumbers:  
        return [stringToNumber(item) for item in rows]
    else:
        return rows

def parseAllNumbersFromSentences(fileName):
    f = open(fileName, "r")
    text = f.read()
    rows = text.split('\n')

    out = []
    for row in rows:
        currList = []
        currString = ""
        for char in row:
            
            if str(char).isnumeric():
                print(char)
                currString += char
            else:
                if len(currString) > 0:
                    currList.append(int(currString))
                currString = ""
            
        if len(currString) > 0:
            currList.append(int(currString))
        out.append(currList)
    return out


def stringToNumber(item):
    if item == "":
        return 0
    return int(item)
