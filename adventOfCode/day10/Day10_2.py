'''
Created on Dec 11, 2017

@author: atip
'''
import numpy


class Day10(object):

    def __init__(self, inputFilename): 
        self.inputFilename = inputFilename
        self.allLenghts = []
        self.totalLength = 256
#         self.totalLength = 5
        self.circularList = list(range(self.totalLength))
        self.crtPos = 0
        self.skipSize = 0
        self.totalRounds = 64
        self.denseList = []
        self.hexedString = ""

    def readInput(self):
        with open(self.inputFilename) as f:
            inputLines = f.readlines()
        self.allLenghts = [ord(crtChar) for crtChar in inputLines[0].strip()]
        self.allLenghts.extend([17, 31, 73, 47, 23])

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
        loopItNo = self.totalRounds
        while loopItNo > 0:
            loopItNo -= 1
            for crtLength in self.allLenghts:
                self.inverseElements(crtLength)
                self.crtPos += crtLength + self.skipSize
                self.crtPos %= self.totalLength
                self.skipSize += 1
            print("crt list: {}, crtPos: {}, skipSize: {}".format(self.circularList, self.crtPos, self.skipSize))
            
    def densifyAndHexIt(self):
        for i in range(16):
            print("crt circularList: {}".format(self.circularList[i*16: i*16 + 16]))
            crtHexedChar =  numpy.bitwise_xor.reduce(self.circularList[i*16: i*16 + 16]) 
            print("crt hexedChar: {}".format(format(crtHexedChar, 'x')))
            self.denseList.append(crtHexedChar)
        self.hexedString = ''.join('%02x'%i for i in self.denseList)

# 462 too low
# day10 = Day10("Day10_example.txt")
day10 = Day10("Day10.txt")
day10.readInput()
print("start with: list: {}, lenghts: {}".format(day10.circularList, day10.allLenghts))
day10.doTheThing()
print("crt circularList : {}".format(day10.circularList))
print("what they want: {}".format(day10.circularList[0] * day10.circularList[1]))
day10.densifyAndHexIt()
print("hexed string: {}".format(day10.hexedString))
listToParse = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
hexedList = numpy.bitwise_xor.reduce(listToParse) 
print("the test example thingie: {}".format(hexedList))


