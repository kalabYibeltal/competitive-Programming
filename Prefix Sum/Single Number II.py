class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mark =  "00000000000000000000000000000000"
        mark2 = "00000000000000000000000000000000"
        num =   "00000000000000000000000000000000"
        
         
        
        countn = 0
        for i in nums:
            # print(bin(i)[1:])
            if i < 0: countn += 1
              
        
        ans = 0       
        if countn%3 == 0:
            j = 31
            mul = 1
            while j > -1:
                count = 0
                for i in nums:
                    if i < 0: 
                        continue
                    s = "0" * (32-len(bin(i)[2:])) +   bin(i)[2:]
                    # s = bin(i)[2:]
                    # print(len(s),s)
                    if s[j] == '1':
                        # print(j)
                        count += 1
                
                # print(count)
                if count%3 == 1: ans = ans + mul
                mul = mul * 2
                
                j = j - 1
                
            return ans
        
        else:
            j = 31
            mul = 1
            while j > -1:
                count = 0
                for i in nums:
                    if i > 0: continue
                    s = "0" * (32-len(bin(i)[3:]))  + bin(i)[3:]
                    print(len(s),s)
                    if s[j] == '1':count += 1
                
                if count%3 == 1: ans = ans + mul
                mul = mul * 2
                
                j = j - 1
            
            return -ans
    
    
