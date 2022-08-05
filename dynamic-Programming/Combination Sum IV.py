class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dictr = {}
        nums.sort()
        for i, num in enumerate(nums):
            if num == target:
                break
        nums= nums[:i+1]
        
        for i,num in enumerate(nums):
            dictr[num] = i  
    
    
        dic = {}
        def count(su,i):
            if (su,i) in dic: return dic[(su,i)]
            
            if i > -1 and su + nums[i] == target: 
                return 1
            if i > -1 and su + nums[i] > target: return 0
            counts = 0
          
            for j in range(len(nums)):
                
                if i == -1: val = count(su,j)
                else: val = count(su+nums[i],j)
                counts += val
                # print(counts)
            
            dic[(su,i)] = counts
            return counts
        
        if nums[0] == target: return 1
        return count(0,-1)
            
