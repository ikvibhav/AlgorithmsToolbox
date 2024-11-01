# Give a target sum and an array of numbers, return a boolean indicating whether or not it is possible to generate the target sum using numbers from the array.
# You may use an element of the array as many times as needed.
# You may assume that all input numbers are nonnegative.

# Time complexity: O(n^m)
# Space complexity: O(m)
def can_sum(target, numbers):
    if target == 0:
        return True
    
    if target < 0:
        return False
    
    for num in numbers:
        if can_sum(target - num, numbers):
            return True
        
    return False

# Time complexity: O(n*m)
# Space complexity: O(m)
def can_sum_memo(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    
    if target == 0:
        return True
    
    if target < 0:
        return False
    
    for num in numbers:
        if can_sum_memo(target - num, numbers, memo):
            memo[target] = True
            return True
    
    memo[target] = False
    return False


if __name__ == "__main__":
    print(can_sum_memo(7, [2, 3], {})) # True
    print(can_sum_memo(7, [5, 3, 4, 7], {})) # True
    print(can_sum_memo(7, [2, 4], {})) # False
    print(can_sum_memo(7, [2, 4], {})) # False
    print(can_sum_memo(300, [7, 14], {})) # False