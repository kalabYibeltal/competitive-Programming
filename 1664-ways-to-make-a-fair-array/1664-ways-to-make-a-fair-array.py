class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        pre = [0,0]
        for n in nums:
            pre.append(pre[-2] + n)
        
        count = 0
        for i in range(len(nums)):
            
            if (len(nums) -1) % 2 == i % 2:
                
                x = pre[-1] - pre[i+2] + pre[i+1]
         
                y = pre[-2] - pre[i+1] + pre[i]
               
            else:
                
                y = pre[-1] -pre[i+1] + pre[i]
           
                x = pre[-2] - pre[i+2] + pre[i+1]
               
            if x == y:
                count += 1
            
        return count
                
                
                        
                        
                        
                    