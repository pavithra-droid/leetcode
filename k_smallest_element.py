import heapq
def k_smallest_element(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, -num)

        if len(heap) > k:
            heapq.heappop(heap)

    return -heap[0]

print(k_smallest_element([2,6,3,1,9], 2))
print(k_smallest_element([1,2,3,4,5], 3))