class fileManager():
    def __init__(self,fileName):
        self.fileName = ''.join(['DaysData/',fileName])
        data = ''
        with open(self.fileName, 'r') as fileOpen:
            data = fileOpen.read()
        print(data)