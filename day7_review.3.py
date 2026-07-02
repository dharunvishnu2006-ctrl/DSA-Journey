def is_valid_max_heap(arr):
    n = len(arr)

    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            return False

        if right < n and arr[i] < arr[right]:
            return False

    return True

arr1 = [9, 5, 6, 1, 2, 3]
arr2 = [5, 9, 6, 1, 2, 3]

print(arr1, "->", is_valid_max_heap(arr1))
print(arr2, "->", is_valid_max_heap(arr2))