def find_first_negative(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            return i
    return None

numbers = [5, 3, -2, 8, -7]
print(find_first_negative(numbers))
