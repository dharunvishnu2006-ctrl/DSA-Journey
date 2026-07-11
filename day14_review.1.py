def count_subset_sum_ways(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1 
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[target]
nums = [1, 1, 2, 3]
target = 4
print(count_subset_sum_ways(nums, target)) 