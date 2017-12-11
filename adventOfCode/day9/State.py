'''
Created on Dec 11, 2017

@author: atip
'''

class State(object):
    
    totalScore = 0
    
    def __init__(self, level = 0):
        self.level = level

    def next(self, crtChar):
        assert 0, "next not implemented"

class Group(State):

    def next(self, crtChar):
        if crtChar == "{":
            State.totalScore += self.level + 1
            return Group(self.level + 1)
        if crtChar == "}":
            return Group(self.level - 1)
        if crtChar == "!":
            return NopGroup(self.level)
        if crtChar == "<":
            return Garbage(self.level)
        return Group(self.level)

class NopGroup(State):

    def next(self, crtChar):
        return Group(self.level)


class Garbage(State):

    def next(self, crtChar):
        if crtChar == ">":
            return Group(self.level)
        if crtChar == "!":
            return NopGarbage(self.level)
        return Garbage(self.level)


class NopGarbage(State):

    def next(self, crtChar):
        return Garbage(self.level)


