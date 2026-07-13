def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0          

    for price in prices:     
        if price < min_price:
            min_price = price    
        else:
            profit = price - min_price   
            if profit > max_profit:
                max_profit = profit    

    return max_profit
prices = [7,1,5,3,6,4]
print(maxProfit(prices))

def isValid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(isValid("()[]{}"))
print(isValid("(]"))

def merge(nums1, m, nums2, n):
    i = m - 1              
    j = n - 1               
    k = m + n - 1          

    while j >= 0:            
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]   
            i -= 1
        else:
            nums1[k] = nums2[j]    
            j -= 1
        k -= 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)        

def climbStairs(n):
    if n <= 2:
        return n                  

    prev2 = 1                     
    prev1 = 2                       

    for i in range(3, n + 1):     
        current = prev1 + prev2    
        prev2 = prev1              
        prev1 = current
    return prev1
print(climbStairs(5))
print(climbStairs(2))

def containsDuplicate(nums):
    seen = set()                  

    for num in nums:
        if num in seen:
            return True           
        seen.add(num)            

    return False                  
print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))