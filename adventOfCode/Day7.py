'''
Created on Dec 7, 2017

@author: atip
'''
import jsonpickle


class Day7(object):
    '''
    classdocs
    '''

    class Program(object):
        
        def __init__(self, name, weight, balancingNames = ()):
            self.name = name
            self.weight = weight
            self.balancingNames = balancingNames
            self.balancing = list()
            self.base = None
        

    def __init__(self, inputFilename):
        self.theTower = {} 
        self.inputFilename = inputFilename
        self.towerBase = None
        
        

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
                
        
    def getBase(self):
        for progName, prog in self.theTower.items():
            if not prog.base:
                return progName
        return None
    
day7 = Day7("Day7_example.txt")
# day7 = Day7("Day7.txt")
day7.readInput()
print("The tower init: {}".format(jsonpickle.encode(day7.theTower)))
day7.stackTower()
print("The tower stacked: {}".format(jsonpickle.encode(day7.theTower)))
base = day7.getBase()
print("Tower base: {}".format(base))

