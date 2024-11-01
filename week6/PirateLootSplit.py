#import numpy as np

# Convert the problem into a knapsack problem
# Why does this not work for 6 1 6 1 6 4?

def PirateLootSplit(PLT_W, PLT_Array):
    PLT_N = len(PLT_Array)
    LootSplit = 0
    PLTMatrix = [[0.0]*(PLT_N+1) for _ in range(PLT_W+1)]
    for i in range(1, PLT_W+1):
        AlreadyUsedi = []
        AlreadyUsedj = []
        #import pdb; pdb.set_trace()
        for j in range(1, PLT_N+1):
            
            if j-1 not in AlreadyUsedj and i not in AlreadyUsedi:
                PLTMatrix[i][j] = PLTMatrix[i][j-1]
            
            if PLT_Array[j-1]<=i and (j-1 not in AlreadyUsedj):
                itracker = i-PLT_Array[j-1]
                if itracker not in AlreadyUsedi:
                    temp = PLTMatrix[itracker][j-1] + PLT_Array[j-1]
                if temp > PLTMatrix[i][j]:
                    PLTMatrix[i][j] = temp
            
            if PLTMatrix[i][j] == PLT_W:
                LootSplit += 1
                AlreadyUsedi.append(itracker)
                AlreadyUsedj.append(j-1)

    if LootSplit < 3: 
        return 0
    return 1

if __name__ == '__main__':
    N = int(input())

    LootArrayStr = input()
    LootArray = [0]*N
    for index in range(N):
        LootArray[index] = (int(LootArrayStr.split()[index]))
    
    TotalLootWeight = sum(LootArray) 

    if N<3: 
        print(0)
    elif TotalLootWeight%3 != 0:
        print(0)
    else:
        print(PirateLootSplit(TotalLootWeight//3, LootArray))