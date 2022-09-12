def naive_fibonacci_lastdigit(n):

    if n == 0 or n == 1:
        return n

    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    for i in range(2,n+1):
        fib_list.append(fib_list[i-2] + fib_list[i-1])
    return fib_list[n]%10

def opti_fibonacci_lastdigit(n):

    if n == 0 or n == 1:
        return n

    fib_iminus2 = 0
    fib_iminus1 = 1
    for i in range(2,n+1):
        fib_i = fib_iminus1%10 + fib_iminus2%10
        fib_iminus2 = fib_iminus1
        fib_iminus1 = fib_i
    
    return fib_i%10
    

if __name__ == "__main__":
    n = input()
    #print(naive_fibonacci_generator(int(n)), optimised_fibonacci_generator(int(n)))
    print(opti_fibonacci_lastdigit(int(n)))