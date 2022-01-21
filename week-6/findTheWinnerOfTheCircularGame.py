def cirr(arr,n,s,k):
    if len(arr)==1:
        return arr[0]
    x=((s-1)+(k%n))%n
    arr.pop(x)
    n=len(arr)
    s=x%n
    return cirr(arr,n,s,k)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i=1
        arr=[]
        while i<=n:
            arr.append(i)
            i+=1
        return cirr(arr,n,0,k)
