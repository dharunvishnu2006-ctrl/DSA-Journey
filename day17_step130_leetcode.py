def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix         
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix        
        suffix *= nums[i]
    return result
print(productExceptSelf([1,2,3,4]))

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:        
            if nums[left] <= target < nums[mid]:
                right = mid - 1              
            else:
                left = mid + 1
        else:                                 
            if nums[mid] < target <= nums[right]:
                left = mid + 1                 
            else:
                right = mid - 1
    return -1
nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums,target))

def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1          
        else:
            right = mid          
    return nums[left]

print(findMin([4,5,6,7,0,1,2]))

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)  
    dp[0] = 0                            

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1,2,5]
amount = 11
print(coinChange(coins,amount))