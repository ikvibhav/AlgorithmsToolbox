from itertools import permutations

def greedy_max_pair_prod(G_n, G_ArrayOne, G_ArrayTwo):
    if G_n == 0:
        return 0
    else:
        #import pdb; pdb.set_trace()
        a = max(G_ArrayOne)
        b = max(G_ArrayTwo)
        G_ArrayOne.remove(a)
        G_ArrayTwo.remove(b)
        G_n -= 1 
        return a*b + greedy_max_pair_prod(G_n,G_ArrayOne, G_ArrayTwo)

def greedy_max_pair_prod_iter(G_n, G_ArrayOne, G_ArrayTwo):
    sum_val = 0
    while G_n != 0: 
        a = max(G_ArrayOne)
        b = max(G_ArrayTwo)
        sum_val += a*b
        G_ArrayOne.remove(a)
        G_ArrayTwo.remove(b)
        G_n -= 1 
    return sum_val        

def greedy_max_pair_prod_iterator(G_n, G_ArrayOne, G_ArrayTwo):
    G_ArrayOne_iterator = permutations(G_ArrayOne)

    G_SumList = []
    for G_SampleIteration in list(G_ArrayOne_iterator):
        G_SumList.append(sum(G_ArrayTwo[i]*G_SampleIteration[i] for i in range(G_n)))
    
    return max(G_SumList)

if __name__ == "__main__":
    n = int(input())
    ArrayOneString = input()
    ArrayTwoString = input()

    ArrayOne = [0]*n
    ArrayTwo = [0]*n

    assert len(ArrayOne) == len(ArrayTwo) == n

    for index in range(n):
        ArrayOne[index] = (int(ArrayOneString.split()[index]))
        ArrayTwo[index] = (int(ArrayTwoString.split()[index]))

    #print(greedy_max_pair_prod(n,ArrayOne,ArrayTwo))
    #print(greedy_max_pair_prod_iterator(n,ArrayOne,ArrayTwo))
    print(greedy_max_pair_prod_iter(n,ArrayOne,ArrayTwo))