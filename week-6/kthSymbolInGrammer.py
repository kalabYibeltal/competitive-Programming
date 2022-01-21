def newn(n,k):
    if n==1:
        return "0"
    if k%2==0:
        val=newn(n-1,k/2)
        if val=="0":
            return "1"
        else:
            return "0"
    else:
        val=newn(n-1,(k+1)/2)
        return val
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return int(newn(n,k))
