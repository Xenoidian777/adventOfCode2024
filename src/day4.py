from helper import fileManager
import re

def checkForString(checkValue,r,c):
    if checkValue == 'XMAS' or checkValue == 'SAMX':
        return True
    return False

def checkForString2(checkValue,r,c):
    if checkValue == 'MAS' or checkValue == 'SAM':
        return True
    return False

#file = fileManager('day4Sample1')
file = fileManager('day4Input')

def part1(file):
    data = file.getRawData().split('\n')
    lengthWord = 4
    maxRow = len(data)
    maxCol = len(data[0])
    counts = 0
    for row, line in enumerate(data):
        upCheck = False if row < lengthWord - 1 else True
        downCheck = False if row > maxRow - lengthWord else True
        for col, char in enumerate(line):
            if char == 'X':
                leftCheck = False if col < lengthWord - 1 else True
                rightCheck = False if col > maxCol - lengthWord else True
                if leftCheck and checkForString(data[row][col - lengthWord +1 :col + 1],row,col):
                    counts +=1
                if leftCheck and upCheck:
                    s = ''.join([data[row-lengthWord + 1][col -lengthWord + 1], data[row-lengthWord + 2][col -lengthWord + 2], data[row-lengthWord + 3][col -lengthWord + 3], data[row-lengthWord + 4][col -lengthWord + 4]])
                    if checkForString(s,row,col):
                        counts += 1
                if leftCheck and downCheck: 
                    s = ''.join([data[row+lengthWord - 1][col -lengthWord + 1], data[row+lengthWord -2][col -lengthWord + 2], data[row+lengthWord -3][col -lengthWord + 3], data[row+lengthWord -4][col -lengthWord + 4]])
                    if checkForString(s,row,col):
                        counts += 1
                if downCheck:
                    s = ''.join([data[row+lengthWord -1][col],data[row+lengthWord -2][col],data[row+lengthWord -3][col],data[row+lengthWord -4][col]])
                    if checkForString(s,row,col):
                        counts += 1
                if rightCheck and downCheck: 
                    s = ''.join([data[row+lengthWord - 1][col +lengthWord - 1], data[row+lengthWord -2][col +lengthWord - 2], data[row+lengthWord -3][col +lengthWord - 3], data[row+lengthWord -4][col +lengthWord - 4]])
                    if checkForString(s,row,col):
                        counts += 1
                if rightCheck and checkForString(data[row][col:col+lengthWord],row,col):
                    counts +=1
                if rightCheck and upCheck: 
                    s = ''.join([data[row-lengthWord + 1][col +lengthWord - 1], data[row-lengthWord + 2][col +lengthWord - 2], data[row-lengthWord + 3][col +lengthWord - 3], data[row-lengthWord + 4][col +lengthWord - 4]])
                    if checkForString(s,row,col):
                        counts += 1
                if upCheck:
                    s = ''.join([data[row-lengthWord +1][col],data[row-lengthWord +2][col],data[row-lengthWord +3][col],data[row-lengthWord +4][col]])
                    if checkForString(s,row,col):
                        counts += 1
    print ("part1",counts)
def part2(file):
    data = file.getRawData().split('\n')
    maxRow = len(data)
    maxCol = len(data[0])
    counts = 0
    for row, line in enumerate(data):
        upDownCheck = True if row > 0 and row < maxRow -1  else False
        for col, char in enumerate(line):
            leftRightCheck = True if col > 0 and col < maxCol -1 else False
            if char == "A" and upDownCheck and leftRightCheck:
                rightDown = ''.join([data[row -1][col-1],data[row][col],data[row+1][col+1]])
                leftDown = ''.join([data[row-1][col+1],data[row][col],data[row+1][col-1]])
                if checkForString2(rightDown,row,col) and checkForString2(leftDown,row,col):
                    counts +=1
    print("part2",counts)
                

part1(file)              
part2(file)
