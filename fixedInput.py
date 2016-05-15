# fixed input 1: read in adjacency matrix
# convert the matrix to a hashtable
# key: a field
# value: other fileds that are adjacent to the field specified by the key
import numpy as np

matrixRowNum = 196
matrixColNum = 2

# read file content and split by linebreaks
with open("data/West_73_units_adjacency.txt") as f:
    content = f.read().splitlines()
    
adj = np.zeros((matrixRowNum, matrixColNum))

for i in range(matrixRowNum):
    adj[i] = [int(x) for x in content[i].split(',')]

keys = adj[:, :-1]
values = adj[:, -1:]

hashTable = {}
key = 1
for i in range(matrixRowNum):
    hashTable.setdefault(key, [])
    if (keys[i][0] == key):
        hashTable[key].append(values[i][0])
    else:
        key += 1
        hashTable.setdefault(key, [])
        hashTable[key].append(int(values[i][0]))

#hashTable
for key in range(1, 74):
    theList = hashTable[key]
    hashTable[key] = [int(j) for j in theList]

for i in range(1,74):
    theList = hashTable[i]
    for j in theList:
        hashTable[j].remove(i)



# fixed input 2: production volumn of each field in three time: time 1, time 2, time 3
volRowNum = 73
volColNum = 5

with open("West_73_units_volumes.txt") as f:
    content = f.read().splitlines()
    
volums = np.zeros((volRowNum, volColNum))

for i in range(volRowNum):
    volums[i] = [float(x) for x in content[i].split(',')]