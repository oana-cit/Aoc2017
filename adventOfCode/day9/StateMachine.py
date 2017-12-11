'''
Created on Dec 11, 2017

@author: atip
'''

class StateMachine(object):
    '''
    classdocs
    '''


    def __init__(self, initialState):
        '''
        Constructor
        '''
        self.currentState = initialState


    # Template method:
    def runAll(self, charStream):
        for crtChar in charStream:
            self.currentState = self.currentState.next(crtChar)
#             print("crtChar: {} => state: {} with level: {}".format(crtChar, self.currentState, self.currentState.level))