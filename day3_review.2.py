import random
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def partition_random(arr, low, high):
    
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)

def quick_sort_random(arr, low, high):
    if low < high:
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]
        pi = partition(arr, low, high)
        quick_sort_random(arr, low, pi - 1)
        quick_sort_random(arr, pi + 1, high)

arr1 = [38, 27, 43, 3, 9, 82, 10]
quick_sort_random(arr1, 0, len(arr1) - 1)
print("Sorted arr1:", arr1)
arr2 = [1, 2, 3, 4, 5, 6, 7]
quick_sort_random(arr2, 0, len(arr2) - 1)
print("Sorted arr2:", arr2)