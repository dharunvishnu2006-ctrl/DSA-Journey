def merge(l1, l2):
    result = []    
    i = 0      
    j = 0         

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]: 
            result.append(l1[i]) 
            i += 1                 
        else:
            result.append(l2[j])
            j += 1   

    result.extend(l1[i:]) 
    result.extend(l2[j:]) 
    return result
l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
print(merge(l1, l2))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2        
    l1  = merge_sort(arr[:mid])  
    l2 = merge_sort(arr[mid:])   
    return merge(l1, l2)
alerts = [38, 27, 43, 3, 9, 82, 10]

print("Before:", alerts)
print("After: ", merge_sort(alerts))