def search_range(arr, target):
    def find_first():
        left, right = 0, len(arr) - 1
        first = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                first = mid
                right = mid - 1  
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return first

    def find_last():
        left, right = 0, len(arr) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                last = mid
                left = mid + 1  
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return last

    return [find_first(), find_last()]