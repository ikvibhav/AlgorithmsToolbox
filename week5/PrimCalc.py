import sys

def PrimCalc_DP(N):
    MinCompDict = {}
    
    MinCompDict[1] = 0
    MinCompDict[2] = 1
    MinCompDict[3] = 1

    for CurrN in range(4,N+1):
        res1 = MinCompDict[CurrN-1]
        res2 = MinCompDict[CurrN//2] if CurrN%2==0 else sys.maxsize
        res3 = MinCompDict[CurrN//3] if CurrN%3==0 else sys.maxsize
        MinCompDict[CurrN] = 1+min(res1,res2,res3)   
    
    Niter = N
    MinCompSeq = [Niter]
    
    while Niter!=1:
        if Niter%3==0 and MinCompDict[Niter]-1==MinCompDict[Niter//3]:
            MinCompSeq += [Niter//3]
            Niter = Niter//3
        elif Niter%2==0 and MinCompDict[Niter]-1==MinCompDict[Niter//2]:
            MinCompSeq += [Niter//2]
            Niter = Niter//2
        else:
            MinCompSeq += [Niter-1]
            Niter = Niter - 1
    
    return MinCompDict[N], MinCompSeq[::-1]
 
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
    NumComps, ComputationList = PrimCalc_DP(N)
    print(NumComps)
    print(*ComputationList)