def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):                      
        for w in range(capacity, weights[i] - 1, -1): 
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]
weights = [3, 5, 6, 4]  
values  = [8, 4, 9, 5]   
capacity = 10
print(knapsack(weights, values, capacity))  

def subset_sum(nums, target):
    n = len(nums)
    dp = [False] * (target + 1)
    dp[0] = True               

    for i in range(n):                          
        for s in range(target, nums[i] - 1, -1):    
            if dp[s - nums[i]]:
                dp[s] = True
    return dp[target]
nums = [100, 200, 500]
target = 700
print(subset_sum(nums, target))  

def can_partition(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False                
    target = total // 2
    return subset_sum(nums, target)   

nums = [1, 5, 11, 5]
print(can_partition(nums))