import random
import math

# fitness calculation class
class FitnessCalc:
    def __init__(self, productionVolum):
        self.target = 34467
        self.colNum = 73
        self.volums = productionVolum
    
    # error calculation of an individual 
    def errorsTotal(self, individual):
        error1 = self.errorInd(individual, 1)
        error2 = self.errorInd(individual, 2)
        error3 = self.errorInd(individual, 3)
        
        return error1 + error2 + error3

    def errorInd(self, individual, phaseNum):
        sum = 0
        for i in range(self.colNum):
            if (individual[i] == phaseNum):
                sum += self.produce(i, phaseNum)
        
        return self.mseCalc(sum)

    def mseCalc(self, theSum):
        return math.pow((theSum - self.target), 2)

    def produce(self, indNum, phaseNum):
        return self.volums[indNum][phaseNum + 1]* self.volums[indNum][1]


# fix adjacency issue class
class Fix:
    def __init__(self, hashTable):
        self.target = 34467
        self.colNum = 73
        self.hashTable = hashTable

    def adjIssues(self, individual):
        theSum = 0
        for i in range(self.colNum):
            if (bool(self.hashTable[i+1]) == False or individual[i] == 0):
                next
            else:
                value = individual[i]
                neighbors = self.hashTable[i+1]
                for j in neighbors:
                    key = j - 1
                    if (individual[key] == value):
                        theSum += 1
        
        return theSum
    
    def fixerIndBefore(self, individual):
        flag = False
        tempInd = list(individual)
        for i in range(self.colNum):
            if (bool(self.hashTable[i+1]) == False or individual[i] == 0):
                next
            else:
                value = individual[i]
                neighbors = self.hashTable[i+1]
            
                for j in neighbors:
                    key = j - 1
                    if (individual[key] == value):
                        tempInd[i] = 0
        
        return tempInd

    def fixerIndAfter(self, individual):
        flag = False
        tempInd = list(individual)
        
        for i in range(self.colNum):
            if (bool(self.hashTable[i+1]) == False or individual[i] == 0):
                next
            else:
                value = individual[i]
                neighbors = self.hashTable[i+1]
            
                for j in neighbors:
                    key = j - 1
                    if (individual[key] == value):
                        tempInd[key] = 0
        
        return tempInd