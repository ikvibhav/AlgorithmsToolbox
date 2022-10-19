import sys
import itertools

#How to obtain the path of the computation sequence?

def GetMinKey(GMK_Dict, GMK_Val):
    for key_i,value_i in GMK_Dict.items():
        if value_i==GMK_Val:
            return key_i

def PrimCalc_DP(N):
    MinCompDict = {}
    ComputationSequenceDict = {}
    
    MinCompDict[1] = 0
    MinCompDict[2] = 1
    MinCompDict[3] = 1

    ComputationSequenceDict[1] = 1
    ComputationSequenceDict[2] = 1
    ComputationSequenceDict[3] = 1

    if N<4:
        return MinCompDict[N], ComputationSequenceDict[N]

    for CurrN in range(4,N+1):
        ind1 = CurrN-1
        ind2 = CurrN//2 if CurrN%2==0 else -1
        ind3 = CurrN//3 if CurrN%3==0 else -2

        SubRes = {}
        SubRes[ind1] = MinCompDict[ind1]
        SubRes[ind2] = MinCompDict[ind2] if ind2>0 else sys.maxsize
        SubRes[ind3] = MinCompDict[ind3] if ind3>0 else sys.maxsize

        MinVal = min(SubRes.values())
        MinValKey = GetMinKey(SubRes, MinVal)

        MinCompDict[CurrN] = 1+MinVal
        ComputationSequenceDict[CurrN] = []
        ComputationSequenceDict[CurrN].append(ComputationSequenceDict[MinValKey])
        ComputationSequenceDict[CurrN].append(MinValKey)
    
    ComputationSequenceDict[N].append(N)

    flat_list = []
    for element in ComputationSequenceDict[N]:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    
    return MinCompDict[N], flat_list


def PrimCalc_Greedy(N):
    PrimCalcList = [0]*(N)
    PrimCalcComputationDict = {}
    
    for i in range(N):
        CurrVal = i+1
        NumOps = 0
        ComputationList = []
        ComputationList.append(CurrVal)

        while CurrVal > 1:
            if CurrVal%3 == 0:
                CurrVal = CurrVal//3
            elif CurrVal%2 == 0:
                CurrVal = CurrVal//2
            else:
                CurrVal = CurrVal - 1
            NumOps += 1
            ComputationList.append(CurrVal)
                
        PrimCalcList[i] = NumOps
        PrimCalcComputationDict[i] = ComputationList
    
    return PrimCalcList[N-1], PrimCalcComputationDict[N-1][::-1]

if __name__ == "__main__":
    N = int(input())
    NumComps,OpsSequence = PrimCalc_DP(N)
    print(NumComps)
    if type(OpsSequence) is list:
        print(*OpsSequence)
    else:
        print(OpsSequence)