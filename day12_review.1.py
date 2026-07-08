def find_all_averages(nums, k):
    if k <= 0 or k > len(nums):
        return []

    result = []
    window_sum = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        if right >= k - 1:
            result.append(window_sum / k)
            window_sum -= nums[left]
            left += 1

    return result