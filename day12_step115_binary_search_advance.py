def search_rotated(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == target:
            return mid
        if arr[lo] <= arr[mid]:          
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                           
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
def find_rotation_minimum(arr):
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if arr[mid] > arr[hi]:
            lo = mid + 1
        else:
            hi = mid

    return arr[lo]

def search_2d_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        row, col = mid // cols, mid % cols
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return False
import math

def min_eating_speed(piles, h):
    lo, hi = 1, max(piles)

    def hours_needed(speed):
        return sum(math.ceil(pile / speed) for pile in piles)

    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            hi = mid
        else:
            lo = mid + 1

    return lo