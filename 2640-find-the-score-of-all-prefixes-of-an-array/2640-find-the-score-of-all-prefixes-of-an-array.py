class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        r_max = 0
        r_sum = 0
        output = []
        
        for num in nums:
            
            r_max = max(r_max, num)
            r_sum = r_sum + r_max + num
            output.append(r_sum)
        
        return output