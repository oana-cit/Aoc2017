'''
Created on Dec 4, 2017

@author: atip
'''
import numpy as np


def hasBeenSeenBefore(newConfig):
    global seenBefore
    for crtConfig in seenBefore:
        if np.all(np.asarray(newConfig) == np.asarray(crtConfig)):
            return True
    return False

def getNewConfig():
    global seenBefore, maxBanks
    newConfig = list(seenBefore[-1])
    maxPos = np.argmax(newConfig)
    redistribute = newConfig[maxPos]
    newConfig[maxPos] = 0
    while redistribute > 0:
        redistribute -= 1
        maxPos += 1
        newConfig[maxPos % maxBanks] += 1
    return newConfig

print("Let us begin!")
theirInput = '''11    11    13    7    0    15    5    5    4    4    1    1    7    1    15    11'''

seenBefore = list()
firstConfig = list(map(int, theirInput.split()))
seenBefore.append(firstConfig)
maxBanks = len(firstConfig)

print("seenBefore: {}".format(seenBefore))

dejaVu = False
totalIterations = 0
while not dejaVu:
    newConfig = getNewConfig()
    dejaVu = hasBeenSeenBefore(newConfig)
    seenBefore.append(newConfig)
    totalIterations += 1
    if totalIterations % 100 == 0:
        print("[{}]".format(totalIterations))

print("totalIterations: {}".format(totalIterations))