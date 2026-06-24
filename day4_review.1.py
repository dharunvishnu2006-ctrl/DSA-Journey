def counting_sort(arr):
    
    minimum = min(arr)
    maximum = max(arr)
    count = [0] * (maximum - minimum + 1)

    for num in arr:
        count[num - minimum] += 1
    result = []
    for i in range(len(count)):
        result.extend([i + minimum] * count[i])

    return result
arr = [4, 2, 8, 3, 1, 7, 4, 2, 9, 1, 5, 3]
print(counting_sort(arr))

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
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    return output

def radix_sort(arr):
    
    maximum = max(arr)
    exp = 1 
    while maximum // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10 
    return arr
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))