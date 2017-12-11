'''
Created on Dec 11, 2017

@author: atip
'''
from filecmp import cmp


class RecvChar(object):

    

    def __init__(self, action):
        self.action = action
    def __str__(self): return self.action
    def __cmp__(self, other):
        return cmp(self.action, other.action)
    # Necessary when __cmp__ or __eq__ is defined
    # in order to make this class usable as a
    # dictionary key:
    def __hash__(self):
        return hash(self.action)
    
# Static fields; an enumeration of instances:
RecvChar.incGroup = RecvChar("{")
RecvChar.decGroup = RecvChar("}")
RecvChar.nop = RecvChar("!")
RecvChar.enterGarbage = RecvChar("<")
RecvChar.leaveGarbage = RecvChar(">")
RecvChar.anyChar = RecvChar("*")

