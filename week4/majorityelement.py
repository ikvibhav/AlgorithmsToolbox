def SortedCheck(SC_arr, SC_n):
    
    # If array has 1 element, then any element will be more than int(1/2) or 0
    if SC_n == 1:
        return 1
    
    SC_arr.sort()
    MajorityVal = int(SC_n/2)
    MajorityCounter = 1
    for i in range(1, len(SC_arr)):
        
        if SC_arr[i-1] == SC_arr[i]:
            MajorityCounter += 1
        else:
            MajorityCounter = 1
        
        if MajorityCounter > MajorityVal:
            return 1
    
    return 0

if __name__ == "__main__":
    MainArraySize = int(input())
    MainArray = list(map(int, input().split()))
    print(SortedCheck(MainArray,MainArraySize))