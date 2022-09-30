def greedy_max_pair_prod(G_n, G_ArrayOne, G_ArrayTwo):
    if G_n == 0:
        return 0
    else:
        a = max(G_ArrayOne)
        b = max(G_ArrayTwo)
        ArrayOne.remove(a)
        ArrayTwo.remove(b)
        G_n -= 1
        return a*b + greedy_max_pair_prod(G_n,ArrayOne, ArrayTwo)
    

if __name__ == "__main__":
    n = int(input())
    ArrayOneString = input()
    ArrayTwoString = input()

    ArrayOne = [0]*n
    ArrayTwo = [0]*n

    for index in range(n):
        ArrayOne[index] = (int(ArrayOneString.split()[index]))
        ArrayTwo[index] = (int(ArrayTwoString.split()[index]))

    print(greedy_max_pair_prod(n,ArrayOne,ArrayTwo))        