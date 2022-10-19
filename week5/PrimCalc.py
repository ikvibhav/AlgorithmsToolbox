import sys

#How to obtain the path of the computation sequence?
def PrimCalc_DP(N):
    MinCompDict = {}
    ComputationSequenceDict = {}
    
    MinCompDict[1] = 0
    MinCompDict[2] = 1
    MinCompDict[3] = 1

    ComputationSequenceDict[1] = [1]
    ComputationSequenceDict[2] = [1,2]
    ComputationSequenceDict[3] = [1,2,3]

    for CurrN in range(4,N+1):
        res1 = MinCompDict[CurrN-1]
        res2 = MinCompDict[CurrN//2] if CurrN%2==0 else sys.maxsize
        res3 = MinCompDict[CurrN//3] if CurrN%3==0 else sys.maxsize
        MinCompDict[CurrN] = 1+min(res1,res2,res3)
    
    return MinCompDict[N]


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
    NumComps = PrimCalc_DP(N)
    print(NumComps)
