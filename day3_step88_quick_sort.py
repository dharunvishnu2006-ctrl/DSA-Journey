def partition(arr, low, high):
    pivot = arr[high]    
    i = low - 1
    for j in range(low, high):    
        if arr[j] <= pivot:     
            i += 1                
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]        
    return i + 1  
arr = [64, 34, 25, 12, 22, 11, 90]
pivot_index = partition(arr, 0, len(arr) - 1)
print("After partition:", arr)
print("Pivot 90 is now at index:", pivot_index)

def quick_sort(arr, low, high):
    if low < high:  
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

models = [64, 34, 25, 12, 22, 11, 90]

print("Before:", models)
quick_sort(models, 0, len(models) - 1)
print("After: ", models)

import random
def partition_random(arr, low, high):
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_random(arr, low, high):
    if low < high:
        pivot_idx = partition_random(arr, low, high)
        quick_sort_random(arr, low, pivot_idx - 1)
        quick_sort_random(arr, pivot_idx + 1, high)

threats = [64, 34, 25, 12, 22, 11, 90]
print("Before:", threats)
quick_sort_random(threats, 0, len(threats) - 1)
print("After: ", threats)

sorted_arr = [1, 2, 3, 4, 5, 6, 7]
print("\nAlready sorted Before:", sorted_arr)
quick_sort_random(sorted_arr, 0, len(sorted_arr) - 1)
print("Already sorted After: ", sorted_arr)