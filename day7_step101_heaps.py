import heapq
nums = [5, 1, 8, 3, 9, 2]

heapq.heapify(nums)
print("Heapified:", nums)

heapq.heappush(nums, 0)
print("After push 0:", nums)
smallest = heapq.heappop(nums)
print("Popped smallest:", smallest)
print("After pop:", nums)

import heapq
def top_k_largest(nums, k):
    return heapq.nlargest(k, nums)

def top_k_smallest(nums, k):
    return heapq.nsmallest(k, nums)

threats = [45, 92, 12, 78, 3, 67, 99, 21]
print("Top 3 most severe:", top_k_largest(threats, 3))
print("Top 3 least severe:", top_k_smallest(threats, 3))

import heapq

def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]

scores = [45, 92, 12, 78, 3, 67, 99, 21]
print("3rd largest:", kth_largest(scores, 3))

import heapq
class MedianFinder:
    def __init__(self):
        self.small = []  
        self.large = []  

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
mf = MedianFinder()
for n in [5, 15, 1, 3]:
    mf.add_num(n)
    print("Median after adding", n, ":", mf.find_median())    