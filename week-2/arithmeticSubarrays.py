class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        i=0
        arr=[]
        while(i<len(l)):
           
            s=nums[l[i]:r[i]+1]
            
            s.sort()
            
            j=2
            boll=True
            if(len(s)>=3):
                x=s[1]-s[0]
                
                while(j<len(s)):
                    if((s[j]-s[j-1])!=x):
                        boll=False
                    j+=1
            arr.append(boll)
            i+=1
        return arr
