def DistinctSummands(DS_n):
    DS = []

    RightPointer = DS_n
    LeftPointer = 1

    while RightPointer > 0:

        if LeftPointer < RightPointer/2:
            DS.append(LeftPointer)
            RightPointer -= LeftPointer
        else:
            DS.append(RightPointer)
            RightPointer = 0

        LeftPointer+=1
    
    return DS

if __name__ == "__main__":
    n = int(input())
    AnswerArray = DistinctSummands(n)
    print(len(AnswerArray))
    print(*AnswerArray)
