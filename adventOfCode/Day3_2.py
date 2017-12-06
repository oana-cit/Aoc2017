'''
Created on Dec 4, 2017

@author: atip
'''

def getAdjSquareSum():
    global posX, posY, valMatrix
    adjSquareSum = 0
    adjSquareSum += valMatrix[maxRange + posX + 1][maxRange + posY]
    adjSquareSum += valMatrix[maxRange + posX + 1][maxRange + posY + 1]
    adjSquareSum += valMatrix[maxRange + posX][maxRange + posY + 1]
    adjSquareSum += valMatrix[maxRange + posX - 1][maxRange + posY + 1]
    adjSquareSum += valMatrix[maxRange + posX - 1][maxRange + posY]
    adjSquareSum += valMatrix[maxRange + posX - 1][maxRange + posY - 1]
    adjSquareSum += valMatrix[maxRange + posX][maxRange + posY - 1]
    adjSquareSum += valMatrix[maxRange + posX + 1][maxRange + posY - 1]
    return adjSquareSum

def getNewCoord(step):
    global posX, posY, theirNumber, crtNumber, valMatrix
    
    if step > 0:
        return theirNumber - crtNumber
    return crtNumber - theirNumber

def checkAndUpdate():
    global posX, posY, theirNumber, maxRange
    crtSum = getAdjSquareSum()
    if crtSum == 0:
        crtSum = 1
        
    print("posX: {}, posY: {}, val: {}".format(posX, posY, crtSum))
        
    valMatrix[maxRange + posX][maxRange + posY] = crtSum
    return crtSum > theirNumber

def goSpiraling(stepX, stepY):
    global posX, posY, theirNumber, crtNumber
#     
#     if theirNumber < crtNumber + abs(stepX):
#         stepX = getNewCoord(stepX)
#     
#     if theirNumber < crtNumber + abs(stepY):
#         stepY = getNewCoord(stepY)
    
    finished = False
    while stepX > 0 and not finished:
        finished = checkAndUpdate()
        posX += 1
        stepX -= 1
    while stepX < 0 and not finished:
        finished = checkAndUpdate()
        posX -= 1
        stepX += 1
    while stepY > 0 and not finished:
        finished = checkAndUpdate()
        posY += 1
        stepY -= 1
    while stepY < 0 and not finished:
        finished = checkAndUpdate()
        posY -= 1
        stepY += 1
        
#     posX += stepX
#     posY += stepY
    crtNumber += abs(stepX) + abs(stepY)
    
    if valMatrix[maxRange + posX][maxRange + posY] > theirNumber:    
        print("reached {} with posX: {}, posY: {}, distance: {}".format(theirNumber, posX, posY, abs(posX) + abs(posY)))
        print("valMatrix: {}".format(valMatrix))
        print("first value written that is larger: {}".format(valMatrix[maxRange + posX][maxRange + posY]))
        return True
    return False


print("Let us begin!")
# theirNumber = 265149  # 438
theirNumber = 1 #0
# theirNumber = 12 #3
# theirNumber = 23 #2
# theirNumber = 1024 #31
valMatrix = [[0 for col in range(200)] for row in range(200)]
maxRange = 100
maxNo = 1
crtStep = 0
lineMax = []
posX = 0
posY = 0
finished = False
crtNumber = 1

valMatrix[maxRange + posX][maxRange + posY] = 1

while not finished:
    finished = goSpiraling(1, 0)
    print("crtNumber {} with posX: {}, posY: {}".format(valMatrix[maxRange + posX][maxRange + posY], posX, posY))
    crtStep += 1
    
    finished = goSpiraling(0, crtStep)
    
    print("crtNumber {} with posX: {}, posY: {}".format(valMatrix[maxRange + posX][maxRange + posY], posX, posY))
    
    crtStep += 1
    finished = goSpiraling(-crtStep, 0)
    print("crtNumber {} with posX: {}, posY: {}".format(valMatrix[maxRange + posX][maxRange + posY], posX, posY))
    finished = goSpiraling(0, -crtStep)
    print("crtNumber {} with posX: {}, posY: {}".format(valMatrix[maxRange + posX][maxRange + posY], posX, posY))
    finished = goSpiraling(crtStep, 0)
    print("crtNumber {} with posX: {}, posY: {}".format(valMatrix[maxRange + posX][maxRange + posY], posX, posY))
    
    lineMax.append(valMatrix[maxRange + posX][maxRange + posY])
    print("Crt progress on step {}: {}".format(valMatrix[maxRange + posX][maxRange + posY], lineMax))
    
#     posY += 1
#         maxNo += 4 * (crtLength - 1)
      
