import heapq
def find_k_largest_using_heap(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

print(find_k_largest_using_heap([1,2,3,4,5], 2))
print(find_k_largest_using_heap([5,6,3,9,1], 3))