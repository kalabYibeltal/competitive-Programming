class Solution(object):
    def numSquarefulPerms(self, nums):
        def back(temp,num,count = 0):
            if len(num)==0:
                return count+1
            for i in range(len(num)):
                if (i>0 and num[i]==num[i-1]) or (len(temp) > 0 and math.sqrt(num[i] + temp[-1]) % 1 != 0):
                    continue
                count = back(temp+[num[i]],num[:i]+num[i+1:],count)
            return count
        
        nums.sort()
        res = back([],nums)
        return res