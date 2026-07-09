def house_robber_circular(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    def house_robber(houses):
        prev2 = 0
        prev1 = 0
        for money in houses:
            current = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current

        return prev1

    return max(
        house_robber(nums[:-1]),  
        house_robber(nums[1:])    
    )
nums = [2, 3, 2]
print(house_robber_circular(nums)) 