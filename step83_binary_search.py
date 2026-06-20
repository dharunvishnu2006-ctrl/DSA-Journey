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
numbers = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(numbers, 50))        
print(binary_search(numbers, 25))