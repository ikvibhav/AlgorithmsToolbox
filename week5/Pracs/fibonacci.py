def NthFibonnaciRecursive(n):
    # Time Complexity - O(2^n)
    # Space Complexity - O(n)    
    if n<=2:
        return 1

    return NthFibonnaciRecursive(n-1) + NthFibonnaciRecursive(n-2)

def NthFibonnaciDp(n, NFD_FibDict = {}):
    if n in NFD_FibDict:
        return NFD_FibDict[n]
    #if also works
    elif n<=2:
        return 1
    NFD_FibDict[n] = NthFibonnaciDp(n-1,NFD_FibDict) + NthFibonnaciDp(n-2,NFD_FibDict)
    return NFD_FibDict[n]

if __name__ == "__main__":
    n = int(input())
    #print(NthFibonnaciRecursive(n))
    print(NthFibonnaciDp(n))