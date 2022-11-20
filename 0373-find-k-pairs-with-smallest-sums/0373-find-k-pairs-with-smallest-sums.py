class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        answer = []
        heap = []
        for n in nums1:
            heappush(heap,[n + nums2[0], n,nums2[0],0])
        
        while len(answer) < k:
            Sum, x, y, z = heappop(heap)
            answer.append([x,y])
            if z + 1 < len(nums2):
                heappush(heap, [x + nums2[z+1], x, nums2[z+1], z+1])
            
            if not heap:
                return answer
        
        return answer
    