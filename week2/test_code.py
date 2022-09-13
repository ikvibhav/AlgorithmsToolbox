import random
import sys
#from fibonacci import *
#from fibonacci_lastdigit import *
from gcd import *
import time

tests = int(sys.argv[1])
value_range = int(sys.argv[2])

for i in range(tests):
    m = random.randint(1,value_range)
    n = random.randint(m,value_range)

    #ans_naive = naive_fibonacci_generator(n)
    #ans_opti = optimised_fibonacci_generator(n)

    start_naive = time.time()
    ans_naive = naive_gcd(m,n)
    dur_naive = round(( time.time() - start_naive ) * 10**6, 2)
    
    start_opti = time.time()
    ans_opti = opti_gcd(m,n)
    dur_opti = round((time.time() - start_opti) * 10**6, 2)
    
    print(f'n= {n} -  {ans_naive}, {ans_opti}    -  {dur_naive}, {dur_opti}')
    if ans_naive != ans_opti:
        break