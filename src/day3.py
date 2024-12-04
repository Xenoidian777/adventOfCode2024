from helper import fileManager
import re

#file = fileManager('day3Sample1')
#file = fileManager('day3Sample2')
file = fileManager('day3Input')

data = file.getRawData()
def part1(data):
    token = 'mul\(\d{1,3}\,\d{1,3}\)'
    mulTokenMatch = re.finditer(token,data)
    numberPairs = []
    for match in mulTokenMatch:
        item = match[0]
        num1 = int(item.split(",")[0].split('(')[1])
        num2 = int(item.split(",")[1].split(")")[0])
        print(num1,num2)
        numberPairs.append([num1,num2])

    sum = 0
    for pair in numberPairs:
        sum += pair[0] * pair[1]
    print(sum) 

def part2(data):
    enable = True
    token = "mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don't\(\)"
    mulTokenMatch = re.finditer(token,data)
    numberPairs = []
    for match in mulTokenMatch:
        item = match[0]
        if item == "do()":
            enable = True
        elif item == "don't()":
            enable = False
        elif enable:
            num1 = int(item.split(",")[0].split('(')[1])
            num2 = int(item.split(",")[1].split(")")[0])
            print(num1,num2)
            numberPairs.append([num1,num2])

    sum = 0
    for pair in numberPairs:
        sum += pair[0] * pair[1]
    print(sum) 

#part1(data)
part2(data)