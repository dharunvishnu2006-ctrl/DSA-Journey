def combination_sum_ii(nums, target):
    nums.sort()
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > remaining:
                break
            path.append(nums[i])
            backtrack(i + 1, path, remaining - nums[i])
            path.pop()
    backtrack(0, [], target)
    return result

nums = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combination_sum_ii(nums, target))
