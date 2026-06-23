import heapq

def top_k_largest(arr, k):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return sorted(min_heap, reverse=True)

threats = [64, 34, 25, 12, 22, 11, 90, 55, 78, 43]
k = 3
print(top_k_largest(threats, k))