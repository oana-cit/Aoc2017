'''
Created on Dec 8, 2017

@author: atip
'''
import operator


class Day8(object):
    '''
    classdocs
    '''

    def __init__(self, inputFilename): 
        self.inputFilename = inputFilename
        self.registers = {}
        self.unusualRegInstructions = None
        self.absoluteMax = 0

    def readInput(self):
        with open(self.inputFilename) as f:
            self.unusualRegInstructions = f.readlines()
        self.unusualRegInstructions = [x.strip() for x in self.unusualRegInstructions] 

    def evalCondition(self, param1, param2, condition):
        return eval(str(param1) + ' ' + condition + ' ' + param2)

    def doOperation(self, param1, param2, crtOp):
        if crtOp == "inc":
            self.registers[param1] += int(param2)
        else:
            self.registers[param1] -= int(param2)
        if self.absoluteMax < self.registers[param1]:
            self.absoluteMax = self.registers[param1]

    def parseInstr(self, instruction):
        tokens = instruction.split()
#         print("tokens: {}".format(tokens))
        # init reg if new
        if not self.registers.get(tokens[0]):
            self.registers[tokens[0]] = 0
        if not self.registers.get(tokens[4]):
            self.registers[tokens[4]] = 0
        # get condition
        if self.evalCondition(self.registers[tokens[4]], tokens[6], tokens[5]):
            self.doOperation(tokens[0], tokens[2], tokens[1])
    
    def executeInstructions(self):
        for crtInstr in self.unusualRegInstructions:
            self.parseInstr(crtInstr)


# day8 = Day8("Day8_example.txt")
day8 = Day8("Day8.txt")
day8.readInput()
# print("start with: {}".format(day8.unusualRegInstructions))
day8.executeInstructions()
print("registers: {}".format(day8.registers))
maxValuePos = max(day8.registers.items(), key=operator.itemgetter(1))[0]
print("maxVal: {}".format(day8.registers[maxValuePos]))
print("absolute max Val: {}".format(day8.absoluteMax))


