class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n%2==0:  
            return int((pow(5,int(n/2),1000000007)*pow(4,int(n/2),1000000007))%(1000000007))        
        else:
            return int((pow(5,int((n+1)/2),1000000007)*pow(4,int(n/2),1000000007))%(1000000007))
