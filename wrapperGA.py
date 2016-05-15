exec(open('fixedInput.py').read())
exec(open('simpleGA.py').read())
exec(open('fitnessMDF.py').read())

class WrapperGa(SimpleGa):

    fix = Fix(hashTable)
    fitness = FitnessCalc(volums)

    # calculate population fitness
    def popFit(self):
        fitVector = [0]*self.rowNum
        for i in range(self.rowNum):
            fitVector[i] = self.indFit(i)
        return fitVector
    
    # calculate individual fitness
    def indFit(self, indNum):
        individual = self.population[indNum]
        errors = self.fitness.errorsTotal(individual)
        return 1/errors

    # fix
    def fixer(self):
        tempInd1 = [0]*self.colNum
        tempInd2 = [0]*self.colNum
        
        for i in range(self.rowNum):
            tempInd1 = fix.fixerIndBefore(self.population[i])
            tempInd2 = fix.fixerIndAfter(self.population[i])
            
            if (self.indFit(tempInd1) > self.indFit(tempInd2)):
                self.population[i] = list(tempInd1)
            else:
                self.population[i] = list(tempInd2)
    
    def evolution(self):
        self.fixer()
        self.indFitVector = self.popFit()
        best = max(self.indFitVector)
        
        limit = 100
        while (limit > 0):
            self.selection()
            self.crossover()
            self.mutation()
            self.fixer()
            self.indFitVector = self.popFit()
            best = max(self.indFitVector)
            limit -= 1
        
        print(best)