from helper import fileManager
import re

#file = fileManager('day5Sample1')
file = fileManager('day5Input')

def changeOrder(update,rules):
    inOrder = True
    newOrder = update
    for rule in rules:
        beforeIdx = update.index(rule['before'])
        afterIdx = update.index(rule['after'])
        if beforeIdx > afterIdx:
            inOrder = False
            newOrder = []
            for i, n in enumerate(update):
                if i not in [afterIdx]:
                    newOrder.append(n)
            newOrder.append(update[afterIdx])
    return newOrder,inOrder
        

def part2(updates, rules):
    sum = 0
    newUpdates = []
    for update in updates:
        newUpdate = update
        setUpdate = set(update)
        rulesToApply = []
        for rule in rules:
            setRule = set(rule['numbers'])
            if setRule.issubset(setUpdate):
                rulesToApply.append(rule)
        inOrder = False
        while not inOrder:
            newUpdate, inOrder = changeOrder(newUpdate,rulesToApply)
        newUpdates.append(newUpdate)
        sum += int(newUpdate[int((len(newUpdate) - 1) / 2)])
    print('Part2', sum)

        
    
def part1(file):
    rules = []
    updates = []
    rawData = file.getRawData().split('\n')
    endRules = False
    for i,row in enumerate(rawData):
        if row == '':
            endRules = True
        else:
            if endRules:
                #Process lines
                update = row.split(',')
                updates.append(update)
            else:
                #Process Rules
                newRuleString = row.split('|')
                rules.append({'before':newRuleString[0],'after':newRuleString[1], 'numbers':[newRuleString[0],newRuleString[1]]})

    sum = 0 
    part2values = []
    for i, update in enumerate(updates):
        valid = True
        setUpdate = set(update)
        for rule in rules:
            setRule = set(rule['numbers'])
            if setRule.issubset(setUpdate):
                beforeIdx = update.index(rule['before'])
                afterIdx = update.index(rule['after'])
                if beforeIdx > afterIdx:
                    if valid:
                        part2values.append(update)
                    valid = False
                    
        if valid:
            sum += int(update[int((len(update) - 1) / 2)])
    print('part1', sum)
    part2(part2values, rules)
part1(file)
            


