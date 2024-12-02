class fileManager():
    def __init__(self,fileName):
        self.fileName = ''.join(['DaysData/',fileName])
        with open(self.fileName, 'r') as fileOpen:
            self.data = fileOpen.read()
    def getRawData(self):
        return (self.data)