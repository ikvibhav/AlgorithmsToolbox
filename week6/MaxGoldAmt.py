import numpy as np

def MaxGold_DPNoReps(MDP_MaxWeight, MDP_GoldArray):
    GoldArrayLen = len(MDP_GoldArray)
    DPMatrix = np.zeros((MDP_MaxWeight+1,GoldArrayLen+1))

    for i in range(1, MDP_MaxWeight+1):
        for j in range(1, GoldArrayLen+1):
            
            DPMatrix[i][j] = DPMatrix[i][j-1]
            if MDP_GoldArray[j-1] <= i:
                TempVal = DPMatrix[i-MDP_GoldArray[j-1]][j-1] + MDP_GoldArray[j-1]

                if TempVal > DPMatrix[i][j]:
                    DPMatrix[i][j] = TempVal
    
    return int(DPMatrix[MDP_MaxWeight][GoldArrayLen])


#Solution works with Knapsack with Repititions
def MaxGold_DPReps(MDP_MaxWeight, MDP_GoldArray):
    MaxWeightList = [0]*(MDP_MaxWeight+1)
    import pdb;pdb.set_trace()

    #Base Case
    MaxWeightList[0] = 0

    for MaxWeighti in range(1, MDP_MaxWeight+1):
        for GoldBarWeight in MDP_GoldArray:

            if GoldBarWeight <= MaxWeighti:
                
                # When MaxWeighti = GoldBarWeight, that means that a Gold bar equals the Gold bar weight to be found
                # In this Case, MinCoinsList[0] is considered
                SubRes = MaxWeightList[MaxWeighti - GoldBarWeight] + GoldBarWeight
                if SubRes > MaxWeightList[MaxWeighti]:
                    MaxWeightList[MaxWeighti] = SubRes
    
    if MaxWeightList[MDP_MaxWeight] == 0:
        return -1
    
    return MaxWeightList

if __name__ == "__main__":
    input_string = input()
    MaxWeight = int(input_string.split()[0])
    GoldBarNum = int(input_string.split()[1])

    GoldBarArray = input()
    GoldArray = [0]*GoldBarNum
    for index in range(GoldBarNum):
        GoldArray[index] = (int(GoldBarArray.split()[index]))
    
    #print(MaxGold_DPReps(MaxWeight, GoldArray))
    print(MaxGold_DPNoReps(MaxWeight, GoldArray))