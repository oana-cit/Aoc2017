'''
Created on Dec 4, 2017

@author: atip
'''

if __name__ == '__main__':
    print("Let us begin!")
    
    theirSum = 0
#     allNumbers = "1122"
#     allNumbers = "1111"
#     allNumbers = "1234"
    allNumbers = "91212129"
    
    for i in range(len(allNumbers) - 1):
        print("i: {}".format(i))
        if allNumbers[i] == allNumbers[i+1]:
            theirSum += int(allNumbers[i])
        
    if allNumbers[len(allNumbers) - 1] == allNumbers[0]:
        theirSum += int(allNumbers[0])
    
    print("Final sum: {}".format(theirSum))