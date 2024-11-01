import argparse

# Method 1
# Time Complexity: O(2^n)
# Space Complexity: O(n)
def fibonacci1(n):
    if n <= 2:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)
    

# Method 2
# Time complexity: O(2^n)
# Space complexity: O(n)
def fibonacci2(n):
    if n <= 2:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)
    

# Method 3 - Dynamic Programming (Memoization)
# Time Complexity: O(n)
# Space Complexity: O(n)
def fibonacci3(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fibonacci3(n-1, memo) + fibonacci3(n-2, memo)

    return memo[n]    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fibonacci sequence")
    parser.add_argument("n", type=int, help="Number of elements in the sequence")
    args = parser.parse_args()

    #print(fibonacci1(args.n))
    #print(fibonacci2(args.n))
    print(fibonacci3(args.n))