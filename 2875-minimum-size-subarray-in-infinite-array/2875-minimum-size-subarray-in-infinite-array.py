class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        remainder = target % total
        val = target // total
        if remainder == 0:
            return val * len(nums)
        pre = [0]
        dic = {0:-1}
        leng  = inf
        
        print(remainder, val)
        for index, n in enumerate(nums):
            pre.append(n + pre[-1])
            if (pre[-1] - (total - remainder)) in dic:
                
                leng = min(leng, len(nums)- ( index - dic[(pre[-1] - (total - remainder))]) )
            if (pre[-1] -  remainder) in dic:
                leng = min(leng,  index - dic[(pre[-1] -  remainder)]  )
            
            dic[pre[-1]] = index
       
        if leng == inf:
            return -1
        return (val * len(nums)) + leng
            