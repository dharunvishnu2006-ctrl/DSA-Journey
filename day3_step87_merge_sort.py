def merge(left, right):
    result = []    
    i = 0      
    j = 0         

    while i < len(left) and j < len(right):
        if left[i] <= right[j]: 
            result.append(left[i]) 
            i += 1                 
        else:
            result.append(right[j])
            j += 1   

    result.extend(left[i:]) 
    result.extend(right[j:]) 
    return result
left  = [10, 30, 50]
right = [20, 40, 60] 
print(merge(left, right))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2        
    left  = merge_sort(arr[:mid])  
    right = merge_sort(arr[mid:])   
    return merge(left, right)
alerts = [64, 34, 25, 12, 22, 11, 90]

print("Before:", alerts)
print("After: ", merge_sort(alerts))

def merge_count(left, right):
    result = []
    inversions = 0     
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
           
            inversions += len(left) - i    
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, inversions 

def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0      

    mid = len(arr) // 2
    left,  left_inv  = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])

    merged, split_inv = merge_count(left, right)
    total = left_inv + right_inv + split_inv

    return merged, total
logs = [64, 34, 25, 12, 22, 11, 90]

sorted_logs, inv_count = count_inversions(logs)
print("Sorted logs:      ", sorted_logs)
print("Total inversions: ", inv_count)