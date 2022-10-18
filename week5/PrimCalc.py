import sys

# def PrimCalc_DP(N):
#     PrimCalcOptions = [1,2,3]
#     PrimCalcList = [sys.maxsize]*(N)
#     PrimCalcComputationDict = {}
    
#     for i in range(N):
#         CurrVal = i+1
#         NumComps = 0
#         ComputationList = []
#         ComputationList.append(CurrVal) 

#         while CurrVal > 1:
#             for Opt in PrimCalcOptions:
#                 if Opt == 1:
#                     SubRes = PrimCalcList[CurrVal-Opt]
#                 elif CurrVal%Opt == 0:
#                     SubRes = PrimCalcList[CurrVal//Opt]
                
#                 if SubRes!= sys.maxsize and SubRes < PrimCalcList[Currval]:
#                     PrimCalcList[Currval] = SubRes + 1
                
#         PrimCalcList[i] = NumComps
#         PrimCalcComputationDict[i] = ComputationList
    
#     return PrimCalcList[N-1], PrimCalcComputationDict[N-1][::-1]

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
    NumComps, CompsList = PrimCalc_Greedy(N)
    print(NumComps)
    print(*CompsList)