'''
Created on Dec 11, 2017

@author: atip
'''

class Day10(object):

    def __init__(self, inputFilename): 
        self.inputFilename = inputFilename
        self.allLenghts = []
        self.totalLength = 256
        self.circularList = list(range(self.totalLength))
        self.crtPos = 0
        self.skipSize = 0

    def readInput(self):
        with open(self.inputFilename) as f:
            inputLines = f.readlines()
        self.allLenghts = list(map(int, inputLines[0].split(',')))
        self.allLenghts = [item for item in self.allLenghts if item <= self.totalLength]

    def inverseElements(self, crtLength):
        startPos = self.crtPos
        stopPos = self.crtPos + crtLength - 1
        while startPos < stopPos:
            aux = self.circularList[startPos % self.totalLength]
            self.circularList[startPos % self.totalLength] = self.circularList[stopPos % self.totalLength]
            self.circularList[stopPos % self.totalLength] = aux
            startPos += 1
            stopPos -= 1

    def doTheThing(self):
        for crtLength in self.allLenghts:
            self.inverseElements(crtLength)
            self.crtPos += crtLength + self.skipSize
            self.crtPos %= self.totalLength
            self.skipSize += 1
            print("crt list: {}, crtPos: {}, skipSize: {}".format(self.circularList, self.crtPos, self.skipSize))
            


# 462 too low
# day10 = Day10("Day10_example.txt")
day10 = Day10("Day10.txt")
day10.readInput()
print("start with: list: {}, lenghts: {}".format(day10.circularList, day10.allLenghts))
day10.doTheThing()
print("crt circularList : {}".format(day10.circularList))
print("what they want: {}".format(day10.circularList[0] * day10.circularList[1]))

