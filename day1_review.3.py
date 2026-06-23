def binary_search(arr, target):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return None
numbers = [1,3,5,7,9,11,13]
print(binary_search(numbers, 7))
print(binary_search(numbers, 24))
