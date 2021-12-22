class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        p=Counter(nums)
        i=0
        count = 0
        while i<len(nums):
            if p[nums[i]]>0:
                p[nums[i]]=p[nums[i]]-1
                if p[k-nums[i]]>0:
                    p[k-nums[i]]=p[k-nums[i]]-1
                    count+=1
            i+=1
        return count
