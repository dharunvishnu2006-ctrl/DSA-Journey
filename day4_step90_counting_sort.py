def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1    
    count = [0] * range_val

    for num in arr:
        count[num - min_val] += 1       
    result = []
    for i, freq in enumerate(count):
        result.extend([i + min_val] * freq)  
    return result

threats = [4, 2, 8, 3, 1, 7, 4, 2, 9, 1, 5, 3]
print("Before:", threats)
print("After: ", counting_sort(threats))

alerts = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("\nAlert priorities Before:", alerts)
print("Alert priorities After: ", counting_sort(alerts))

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n       
    count = [0] * 10        
    for num in arr:
        digit = (num // exp) % 10  
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)   
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10             

    return arr

experiments = [170, 45, 75, 90, 802, 24, 2, 66]
print("Before:", experiments)
radix_sort(experiments)
print("After: ", experiments)

threat_ids = [329100, 457801, 112903, 678234, 234567, 901234]
print("\nThreat IDs Before:", threat_ids)
radix_sort(threat_ids)
print("Threat IDs After: ", threat_ids)

def bucket_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        
        index = int((num - min_val) / (max_val - min_val + 1) * n)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()      
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result
alerts = [0.42, 0.32, 0.91, 0.15, 0.67, 0.55, 0.78, 0.23]
print("Before:", alerts)
print("After: ", bucket_sort(alerts))

models = [0.92, 0.87, 0.95, 0.78, 0.99, 0.83, 0.91]
print("\nModel scores Before:", models)
print("Model scores After: ", bucket_sort(models))