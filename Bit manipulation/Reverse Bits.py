class Solution:
    def reverseBits(self, n: int) -> int:
       
        s = str(bin(n)[2:])
#         # print(bin(n))
#         ans = ""
#         for i in range(len(s)):
#             ans += s[len(s)-1-i]
        
        mul = 1
        num = 0
        l = ""
        x = 32 - len(s)
        for i in range(0,x):
            l += '0'
        s = l + s
        for i in range(0,len(s)):
            # l += s[i]
            num += int(s[i]) * mul
            mul = mul * 2
        
        # print(l)
        return num
    
        
        
