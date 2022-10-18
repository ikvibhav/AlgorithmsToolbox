def GridTravellerRecursive(m,n,DpMem = {}):
    KeyVal = f'{m},{n}'
    if KeyVal in DpMem:
        return DpMem[KeyVal]
    if m==0 or n ==0:
        return 0
    if m==1 and n==1:
        return 1
    DpMem[KeyVal] = GridTravellerRecursive(m-1,n,DpMem) + GridTravellerRecursive(m,n-1,DpMem)
    return DpMem[KeyVal]

if __name__ == "__main__":
    print(GridTravellerRecursive(1,1))
    print(GridTravellerRecursive(3,2))
    print(GridTravellerRecursive(3,3))
    print(GridTravellerRecursive(18,18))