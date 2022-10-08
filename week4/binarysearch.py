def NaiveSearch(NS_arr, NS_key):
    for i in range(len(NS_arr)):
        if NS_arr[i] == NS_key:
            return i
    return -1        

def BinarySearch(BS_arr, BS_key):
    MinIndex = 0
    MaxIndex = len(BS_arr) - 1
    
    while MinIndex <= MaxIndex:
        MidIndex = int((MinIndex+MaxIndex)/2)
        if BS_key == BS_arr[MidIndex]:
            return MidIndex
        elif BS_key > BS_arr[MidIndex]:
            MinIndex = MidIndex+1
        else:
            MaxIndex = MidIndex-1

    return -1   

if __name__ == "__main__":
    MainArraySize = int(input())
    MainArray = list(map(int, input().split()))
    KeyArraySize = int(input())
    KeyArray = list(map(int, input().split()))
    ReturnList = []

    for KeyVal in KeyArray:
        ReturnList.append(BinarySearch(MainArray,KeyVal))

    print(*ReturnList) 