def invrt(n:str) -> str:
    k=len(n)
    i=0
    s=""
    while i<k:
        if n[i]=='0':
            s=s+'1'
        else:
            s=s+'0' 
        i+=1
    return s
def revrs(n:str) -> str:
    k=len(n)
    i=0
    s=""
    while i<k:
        s=s+n[k-1-i]
        i+=1
    return s
def maine(n,s,k,m):
    if m==s:
        return n[k-1]
    else:
        return maine( n + '1' + revrs(invrt(n)),s,k,m+1)
          
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        m=1
        return maine('0',n,k,m)
