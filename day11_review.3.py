def remove_duplicates_sorted(arr):
    if not arr:
        return 0
    slow = 0

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1
arr = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates_sorted(arr)
print(length)       
print(arr[:length])  