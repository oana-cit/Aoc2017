'''
Created on Dec 11, 2017

@author: atip
'''
from adventOfCode.day9.State import Group, State
from adventOfCode.day9.StateMachine import StateMachine


# charStream = '''{}''' # gr: 1, score: 1
# charStream = '''{{{}}}''' # gr: 3, score: 6
# charStream = '''{{},{}}''' # gr: 3, score: 6
# charStream = '''{{{},{},{{}}}}''' # gr: 6, score: 16
# charStream = '''{<{},{},{{}}>}''' # gr: 1, score: 1
# charStream = '''{{<a!>},{<a!>},{<a!>},{<ab>}}''' # gr: ?, score: 3


# inputFileName = "Day9_example.txt"
inputFileName = "Day9.txt"

with open(inputFileName) as f:
    allLines = f.readlines()
allLines = [x.strip() for x in allLines]


for crtCharStream in allLines:
    State.totalRemovedGarbage = 0
    State.totalScore = 0
    stateMachine = StateMachine(Group())
    stateMachine.runAll(crtCharStream)
#     print("Crt input: {}".format(crtCharStream))
    print("total score: {}".format(State.totalScore))
    print("total removed garbage: {}".format(State.totalRemovedGarbage))