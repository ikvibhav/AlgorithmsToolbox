import sys

#How to Obtain the sequence of numbers being multiplied?
#This solution needs to compute PrimCalcDP(n-1) from n until 1
# When n is very large (>90000), then there are 995 recursive calls made 
# and the recursion stack gets exhausted
# Thus, taking a bottom to top approach maybe required
def PrimCalcDP(n, MemoDict = {}):
    if n in MemoDict:
        return MemoDict[n]
    if n == 1:
        return 0
    if n==2 or n==3:
        return 1
    
    res1 = sys.maxsize
    res2 = sys.maxsize
    res3 = sys.maxsize

    res1 = 1+PrimCalcDP(n-1,MemoDict)
    if n%2 == 0:
        res2 = 1+PrimCalcDP(n//2,MemoDict)
    if n%3 == 0:
        res3 = 1+PrimCalcDP(n//3,MemoDict)
    
    MemoDict[n] = min(res1,res2,res3)
    return MemoDict[n]  


def PrimCalcRecursive(n):
    if n == 1:
        return 0
    if n==2 or n==3:
        return 1
    
    res1 = sys.maxsize
    res2 = sys.maxsize
    res3 = sys.maxsize

    res1 = 1+PrimCalcRecursive(n-1)
    if n%2 == 0:
        res2 = 1+PrimCalcRecursive(n//2)
    if n%3 == 0:
        res3 = 1+PrimCalcRecursive(n//3)
    
    return min(res1,res2,res3)       

if __name__ == "__main__":
    N = int(input())
    NumComps = PrimCalcDP(N)
    print(NumComps)