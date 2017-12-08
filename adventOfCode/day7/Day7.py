'''
Created on Dec 7, 2017

@author: atip
'''
from collections import Counter
import jsonpickle


class Day7(object):
    '''
    classdocs
    '''

    class Program(object):
        
        def __init__(self, name, weight, balancingNames = ()):
            self.name = name
            self.weight = weight
            self.realWeight = weight
            self.balancingNames = balancingNames
            self.balancing = list()
            self.base = None
        

    def __init__(self, inputFilename):
        self.theTower = {} 
        self.inputFilename = inputFilename
        self.towerBase = None
        self.fix = 0
        
    def readInput(self):
        with open(self.inputFilename) as f:
            content = f.readlines()
        content = [x.strip() for x in content] 
        for crtProgram in content:
            description = crtProgram.split()
            name = description[0]
            weight = int(description[1][1:-1])
            balancingNames = list(map(lambda each:each.strip(","), description[3:]))
            self.theTower[name] = self.Program(name, weight, balancingNames)

    def stackTower(self):
        '''
        Link balancing programs to base and return base.
        '''
        for progName, prog in self.theTower.items():
            for balancedProgName in prog.balancingNames:
                self.theTower.get(balancedProgName).base = self.theTower.get(progName)
                self.theTower.get(progName).balancing.append(self.theTower.get(balancedProgName))
                
        
    def setBase(self):
        for progName, prog in self.theTower.items():
            if not prog.base:
                self.towerBase = prog
                return progName
        return None

    def getRealWeight(self, crtProg):
        if not crtProg.balancing:
            return crtProg.weight
        balancedWeight = 0
        childWeights = {}
        for balancedProg in crtProg.balancing:
            crtWeight = self.getRealWeight(balancedProg)
            balancedWeight += crtWeight
            if not childWeights.get(crtWeight):
                childWeights[crtWeight] = list()
                childWeights[crtWeight].append(balancedProg.name)
            else:
                childWeights[crtWeight].append(balancedProg.name)
        
        crtProg.realWeight += balancedWeight

        if len(childWeights) > 1:
            print("crt prog {} has: {}".format(crtProg.name, childWeights))
            # hack => assume only 2
            actualVals = list(childWeights.keys())
            keysDiff = abs(actualVals[0] - actualVals[1])
            if len(childWeights[actualVals[0]]) < len(childWeights[actualVals[1]]):
                wrongProg = self.theTower[childWeights[actualVals[0]][0]]
            else:
                wrongProg = self.theTower[childWeights[actualVals[1]][0]]
            print("prog: {} should be: {} - {} = {}".format(wrongProg.name, wrongProg.weight, keysDiff, wrongProg.weight - keysDiff))
            assumeOnly2 = actualVals[0] - actualVals[1] 
            print("==>>  crt prog {} has: {}; {}".format(crtProg.name, crtProg.weight - abs(assumeOnly2), assumeOnly2))
        return crtProg.realWeight


# day7 = Day7("Day7_example.txt")
day7 = Day7("Day7.txt")
day7.readInput()
# print("The tower init: {}".format(jsonpickle.encode(day7.theTower)))
day7.stackTower()
# print("The tower stacked: {}".format(jsonpickle.encode(day7.theTower)))
base = day7.setBase()
print("Tower base: {}".format(base))
base = day7.getRealWeight(day7.towerBase)
# print("The tower weighted: {}".format(jsonpickle.encode(day7.theTower)))
print("Tower base: {}".format(base))
