from helper import fileManager

class level():
    '''
    Advent of code Day 2 level
    provide a list of int for levelData and number of failures allowed (not fully functioning above the count of 1)
    
    '''
    def __init__(self,levelData -> [], failuresAllowed = 0):
        self.failuresAllowed = failuresAllowed
        self.failuresDetected = 0
        self.levelData = levelData
        self.safe = True
        if levelData[0] > levelData[1]:
            self.decreasing = True
            self.increasing = False
        elif levelData[0] < levelData[1]:
            self.decreasing = False
            self.increasing = True
        else:
            self.safe = False
        self._check_safety()
        
    def _check_safety(self):
        if self.safe:
            firstItem = self.levelData[0]
            for item in range(1,len(self.levelData)):
                steps = self.levelData[item] - firstItem
                holding = firstItem
                firstItem = self.levelData[item]
                if self.decreasing:
                    if steps not in [-1,-2,-3]:
                        if self._check_failure():
                            break
                        else:
                            firstItem = holding
                else:
                    if steps not in [1,2,3]:
                        if self._check_failure():
                            break
                        else:
                            firstItem = holding
    
    def _check_failure(self):
        self.failuresDetected +=1
        if self.failuresAllowed < self.failuresDetected:
            self.safe = False
            return True
        return False
    def get_Status(self):
        return self.safe

def part1():
    count = 0
    #file = fileManager('day2Sample1')
    file = fileManager('day2Input')

    rowData = file.getRawData().split('\n')
    data = []
    for row in rowData:
        raw = row.split()
        processedRow = []
        for item in raw:
            processedRow.append(int(item))
        data.append(processedRow)

    for row in data:
        test = level(row)
        if test.get_Status():
            count +=1
        else:
            print(test.levelData)
    print(count)

def part2(ra):
    count = 0
    #file = fileManager('day2Sample1')
    file = fileManager('day2Input')

    rowData = file.getRawData().split('\n')
    data = []
    for row in rowData:
        raw = row.split()
        processedRow = []
        for item in raw:
            processedRow.append(int(item))
        data.append(processedRow)

    for row in data:
        test = level(row,ra)
        if test.get_Status():
            count +=1
        else:
            found = False
            print(test.levelData)
            print('searching')
            for i in range(0,len(row)): #originally had 1 to len(row) - 1  this did not work changing to 0 to len(row) allowed it to function correctly. 
                newRow = row.copy()
                del newRow[i]
                print('     ',newRow)
                t = level(newRow)
                if t.get_Status():
                    found = True
                    count +=1
                    print('     found') 
                    break
            if not found:
                print('Not Found')
    print(count)

#part1()
#main(1) #562 is too low #569 is to low Issue found 
part2(1)





    
