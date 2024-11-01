# Given a grid of size (n,m), find the number of ways to travel from the top-left corner to the bottom-right corner. 
# You can only move down or right.

import argparse


# Memoization
# Time Complexity: O(m*n)
# Space Complexity: O(m+n)
def grid_traveller(m, n, memo={}):
    key = str(m) + "," + str(n)

    if key in memo:
        return memo[key]
    
    if m == 1 and n == 1:
        return 1
    
    if m == 0 or n == 0:
        return 0
    
    memo[key] = grid_traveller(m-1, n, memo) + grid_traveller(m, n-1, memo)

    return memo[key]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Grid Traveller")
    parser.add_argument("m", type=int, help="Number of rows")
    parser.add_argument("n", type=int, help="Number of columns")
    args = parser.parse_args()

    print(grid_traveller(args.m, args.n))