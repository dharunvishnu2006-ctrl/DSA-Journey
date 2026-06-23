def heapify(arr, n, i):
    largest = i          
    left  = 2 * i + 1   
    right = 2 * i + 2  
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]   
        heapify(arr, n, largest)    
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Before heapify:", arr)
heapify(arr, n, 2)
print("After heapify at index 2:", arr)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    print("After building max heap:", arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
threats = [12, 11, 13, 5, 6, 7]

print("Before heap sort:", threats)
heap_sort(threats)
print("After heap sort: ", threats)

import heapq
def top_k_largest(arr, k):
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, num)   
        
        if len(min_heap) > k:            
            heapq.heappop(min_heap)     
    
    return sorted(min_heap, reverse=True)  
def top_k_smallest(arr, k):
   
    return heapq.nsmallest(k, arr)
threats = [64, 34, 25, 12, 22, 11, 90, 55, 78, 43]
k = 3

print("All threats:        ", threats)
print("Top 3 most severe:  ", top_k_largest(threats, k))
print("Top 3 least severe: ", top_k_smallest(threats, k))

models = [0.92, 0.87, 0.95, 0.78, 0.99, 0.83, 0.91]
print("\nAll model scores:   ", models)
print("Top 3 best models:  ", top_k_largest(models, 3))