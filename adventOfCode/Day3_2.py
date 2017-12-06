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

def check():
    global posX, posY, theirNumber, maxRange, valMatrix
    found = valMatrix[maxRange + posX][maxRange + posY] > theirNumber 
    if found:
        print("[{}][{}] +++> {}".format(posX, posY, valMatrix[maxRange + posX][maxRange + posY]))
    return found

def checkAndUpdate():
    global posX, posY, theirNumber, maxRange, valMatrix
    crtSum = getAdjSquareSum()
    if crtSum == 0:
        crtSum = 1
    
    valMatrix[maxRange + posX][maxRange + posY] = crtSum    
    print("[{}][{}] => {}".format(posX, posY, crtSum))
    
    return check()

def goSpiraling(stepX, stepY):
    global posX, posY, theirNumber, maxRange, valMatrix
 
    finished = False
    while stepX > 0 and not finished:
        print("stepX > 0 : stepX: {}, posX: {}".format(stepX, posX))
        posX += 1
        stepX -= 1
        finished = checkAndUpdate()
#         finished = True
    while stepX < 0 and not finished:
        print("stepX < 0 : stepX: {}, posX: {}".format(stepX, posX))
        posX -= 1
        stepX += 1
        finished = checkAndUpdate()
#         finished = True
    while stepY > 0 and not finished:
        print("stepY > 0 : stepY: {}, posY: {}".format(stepY, posY))
        posY += 1
        stepY -= 1
        finished = checkAndUpdate()
#         finished = True
    while stepY < 0 and not finished:
        print("stepY < 0 : stepY: {}, posY: {}".format(stepY, posY))
        posY -= 1
        stepY += 1
        finished = checkAndUpdate()
#         finished = True
   
    if valMatrix[maxRange + posX][maxRange + posY] > theirNumber:
        return check()
    
    return False


print("Let us begin!")
theirNumber = 265149  # 438
# theirNumber = 1 #0
# theirNumber = 747
valMatrix = [[0 for col in range(200)] for row in range(200)]
maxRange = 100
maxNo = 1
crtStep = 0
posX = 0
posY = 0
finished = False
crtNumber = 1

valMatrix[maxRange + posX][maxRange + posY] = 1

while not finished:
    finished = goSpiraling(1, 0)
    crtStep += 1
    if not finished:
        finished = goSpiraling(0, crtStep)
    
    crtStep += 1
    if not finished:
        finished = goSpiraling(-crtStep, 0)
    if not finished:
        finished = goSpiraling(0, -crtStep)
    if not finished:
        finished = goSpiraling(crtStep, 0)
    
    print("[{}][{}] ==>> {}".format(posX, posY, valMatrix[maxRange + posX][maxRange + posY]))
      
