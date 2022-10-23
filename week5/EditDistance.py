import numpy as np

def EditDistance_DP(ED_A, ED_B):
    LenA = len(ED_A)
    LenB = len(ED_B)

    #Init the Computation Matrix
    Matrix = np.zeros((LenA+1 , LenB+1))

    #Insertion Case, D(0,i) = i
    for i in range(LenB+1):
        Matrix[0][i] = i

    #Deletion Case, D(i,0) = i
    for i in range(LenA+1):
        Matrix[i][0] = i

    # Filling the matrix
    for i in range(1, LenA+1):
        for j in range(1, LenB+1):
            insertion = Matrix[i][j-1]   + 1
            deletion  = Matrix[i-1][j]   + 1
            mismatch  = Matrix[i-1][j-1] + 1
            match     = Matrix[i-1][j-1]
            if ED_A[i-1] == ED_B[j-1]:
                Matrix[i][j] = min(insertion, deletion, match)
            if ED_A[i-1] != ED_B[j-1]:
                Matrix[i][j] = min(insertion, deletion, mismatch)
    
    return int(Matrix[LenA][LenB])

if __name__ == '__main__':
    A = input()
    B = input()
    print(EditDistance_DP(A, B))