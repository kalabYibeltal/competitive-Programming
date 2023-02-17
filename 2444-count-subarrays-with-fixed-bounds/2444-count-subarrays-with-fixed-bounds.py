class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int: 
        i=0 
        j=0 
        c=0 
        mi=-1 
        ma=-1 
        while j<len(nums): 
            while j<len(nums): 
                if not(minK<=nums[j]<=maxK): 
                    break
             
                if nums[j]==minK: 
                    mi=j
                if nums[j]==maxK: 
                    ma=j
                if mi!=-1 and ma!=-1: 
                    c+=(min(mi,ma)-i+1)
                j+=1
            j+=1 
            i=j
            mi=-1 
            ma=-1 
        return c
            