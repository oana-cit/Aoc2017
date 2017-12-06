'''
Created on Dec 4, 2017

@author: atip
'''

def getNewCoord(step):
    global posX, posY, theirNumber, crtNumber
    
    if step > 0:
        return theirNumber - crtNumber
    return crtNumber - theirNumber

def goSpiraling(stepX, stepY):
    global posX, posY, theirNumber, crtNumber
    
    if theirNumber < crtNumber + abs(stepX):
        stepX = getNewCoord(stepX)
    
    if theirNumber < crtNumber + abs(stepY):
        stepY = getNewCoord(stepY)
        
    posX += stepX
    posY += stepY
    crtNumber += abs(stepX) + abs(stepY)
    
    if crtNumber == theirNumber:    
        print("reached {} with posX: {}, posY: {}, distance: {}".format(theirNumber, posX, posY, abs(posX) + abs(posY)))
        return True
    return False


print("Let us begin!")
theirNumber = 265149 #438
# theirNumber = 1 #0
# theirNumber = 12 #3
# theirNumber = 23 #2
# theirNumber = 1024 #31
maxNo = 1
crtStep = 0
lineMax = []
posX = 0
posY = 0
finished = False
crtNumber = 1
while not finished:
    
    finished = goSpiraling(1, 0)
    print("crtNumber {} with posX: {}, posY: {}, distance: {}".format(crtNumber, posX, posY, abs(posX) + abs(posY)))
    crtStep += 1
    
    finished = goSpiraling(0, crtStep)
    
    print("crtNumber {} with posX: {}, posY: {}, distance: {}".format(crtNumber, posX, posY, abs(posX) + abs(posY)))
    
    crtStep += 1
    finished = goSpiraling(-crtStep, 0)
    print("crtNumber {} with posX: {}, posY: {}, distance: {}".format(crtNumber, posX, posY, abs(posX) + abs(posY)))
    finished = goSpiraling(0, -crtStep)
    print("crtNumber {} with posX: {}, posY: {}, distance: {}".format(crtNumber, posX, posY, abs(posX) + abs(posY)))
    finished = goSpiraling(crtStep, 0)
    print("crtNumber {} with posX: {}, posY: {}, distance: {}".format(crtNumber, posX, posY, abs(posX) + abs(posY)))
    
    lineMax.append(crtNumber)
    print("Crt progress on step {}: {}".format(crtNumber, lineMax))
    
#     posY += 1
#         maxNo += 4 * (crtLength - 1)
      