import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        i=0
        while i<len(nums):
            if len(heap)<k:
                heapq.heappush(heap,nums[i])
            elif nums[i]>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])
            i+=1
        return heap[0]