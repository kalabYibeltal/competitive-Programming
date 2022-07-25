class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l = r = 0
        summ = 0
        while r < min(k,len(nums)):
            ans.append(-1)
            summ += nums[r]
            r += 1
        

        while r < min(len(nums),2*k + 1):
            # print(r)
            summ += nums[r]
            avg = summ/ (2*k + 1)
            r += 1
        
        
        while r < (len(nums)):
            ans.append(int(avg))
            summ -= nums[l]
            summ += nums[r]
            avg = summ/ (2*k + 1)
            l += 1
            r += 1
        
        if len(ans) < len(nums) and len(nums) < (len(ans) + k + 1):  ans.append(-1)
        elif len(ans) < len(nums): ans.append(int(avg))
        while len(ans) < (len(nums)):
            ans.append(-1)
            l += 1
        
        return ans
