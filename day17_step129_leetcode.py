def threeSum(nums):
    nums.sort()                      
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                

        if nums[i] > 0:
            break                   
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1         
            elif total > 0:
                right -= 1           
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1      
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1       
    return result
print(threeSum([-1,0,1,2,-1,-4]))

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])   
        current_area = width * current_height
        max_water = max(max_water, current_area)

        if height[left] < height[right]:
            left += 1           
        else:
            right -= 1              
    return max_water
print(maxArea( [1,8,6,2,5,4,8,3,7]))

def lenghtOfLongestSubstring(s):
    seen = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]

        if char in seen and seen[char] >= left:
            left = seen[char] + 1       

        seen[char] = right              
        max_length = max(max_length, right - left + 1)
    return max_length

print(lenghtOfLongestSubstring("abcabcbb"))

def groupAnagrams(strs):
    groups = {}                       
    for word in strs:
        key = ''.join(sorted(word))   

        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))