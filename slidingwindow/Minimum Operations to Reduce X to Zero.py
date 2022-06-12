class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
  
        ans = 0
        l = r = 0
        s = sum(nums)
        target = s - x
        if target == 0: return len(nums)
        if target < 0: return -1
        if x < min(nums): return -1
        su = 0
        while l < len(nums):
            if su == target and (r-l) > ans: 
                ans = r-l
            if r == len(nums): break
            su += nums[r]
            # print(r,su)
            while su > target:
                su -= nums[l]
                l += 1
            # print(su)
            r += 1
            
        print(ans)
        if ans == 0: return -1
        return len(nums) - ans
            
            
            
            
# faile bfs algorithm because the question cannot be solved using bfs
        # print(que)
#         [0,len(nums)-1]
#         while True:
#             print(que)
#             i,level,val,pos=que.popleft()
#             if level == len(nums): return -1
#             if val == x: return level
#             if val > x: continue
#             if pos == 0:
#                 que.append([i+1,level+1,val+nums[i+1],0])
#                 que.append([v[-1],level+1,val+nums[v[-1]],1])
#             if pos == 1:
#                 que.append([i-1,level+1,val+nums[i-1],1])
#             # print(que)
        
#         return level
