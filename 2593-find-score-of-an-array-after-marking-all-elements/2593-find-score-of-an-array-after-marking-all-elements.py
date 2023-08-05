class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [[nums[i],i] for i in range(len(nums))]
        heapify(heap)
        
        marked = set()
        total = 0
        
        while heap:
            val, index = heappop(heap)
            if index not in marked:
                marked.add(index)
                if index < len(nums) - 1: marked.add(index + 1)
                if index > 0: marked.add(index - 1)
                total += val
        
        return total