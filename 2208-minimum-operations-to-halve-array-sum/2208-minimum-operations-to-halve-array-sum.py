class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        half = total / 2
        heap = []
        for num in nums: heappush(heap, -num)
        count = 0
        while total > half:
            num = heappop(heap)
            total += (num/2)
            heappush(heap, num/2)
            count += 1
        
        return count