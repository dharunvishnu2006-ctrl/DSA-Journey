def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr [j]
                swapped = True

        if not swapped:
            break
    return arr
numbers = [64, 25, 12, 22, 11]
print(bubble_sort(numbers))
