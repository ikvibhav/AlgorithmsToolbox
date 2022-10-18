import sys

#How to Obtain the sequence of numbers being multiplied?
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
    NumComps = PrimCalcRecursive(N)
    print(NumComps)