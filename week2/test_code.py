import random
import sys
from maxseqpairprod import *
import time
import numpy as np

Tests = int(sys.argv[1])
ListRange = int(sys.argv[2])
ListSize = int(sys.argv[3])

for i in range(Tests):

    ListOne = list(np.random.randint(1,ListRange,ListSize))
    ListTwo = list(np.random.randint(1,ListRange,ListSize))

    start_naive = time.time()
    ans_naive = greedy_max_pair_prod_iterator(ListSize,ListOne,ListTwo)
    dur_naive = round(( time.time() - start_naive ) * 10**6, 2)
    
    start_opti = time.time()
    ans_opti = greedy_max_pair_prod_iter(ListSize,ListOne,ListTwo)
    dur_opti = round((time.time() - start_opti) * 10**6, 2)
    
    print(f'Iteration= {i} -  {ans_naive}, {ans_opti}    -  {dur_naive}, {dur_opti}')
    if ans_naive != ans_opti:
        break