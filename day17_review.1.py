def twoSumSorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [nums[left], nums[right]]
        elif total < target:
            left += 1  
        else:
            right -= 1  
    return []
nums = [1, 2, 4, 6, 10]
target = 8

print(twoSumSorted(nums, target))

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
    return all(value == 0 for value in count.values())

print(isAnagram("listen", "silent"))
print()