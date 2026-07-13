def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]            

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i]) 
        max_sum = max(max_sum, current_sum)                 

    return max_sum
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

def missingNumber(nums):
    n = len(nums)
    result = n            

    for i in range(n):
        result ^= i              
        result ^= nums[i]         

    return result                 
print(missingNumber([3,0,1]))
print(missingNumber([0,1]))

def singleNumber(nums):
    result = 0                

    for num in nums:
        result ^= num          

    return result
print(singleNumber([4,1,2,1,2]))

def moveZeroes(nums):
    write = 0                      

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]   
            write += 1

    for i in range(write, len(nums)):
        nums[i] = 0                   

    return nums
print(moveZeroes([0,1,0,3,12]))

def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num          
        count += 1 if num == candidate else -1  

    return candidate

print(majorityElement( [2,2,1,1,1,2,2]))