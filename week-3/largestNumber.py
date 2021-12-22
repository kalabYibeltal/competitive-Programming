class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr=[]
        dictr={}
        for c in nums:
            z=str(c)
            y=len(z)
            x=z*9
            x=x[ :9]
            if x in dictr:
                dictr[x].append(z)
            else:
                dictr[x]=[z]
        q=sorted(dictr)
        q.sort(reverse=True)
        d=""
        for c in q:
            i=0
            arr=dictr[c]
            while i<len(arr):
                d=d+arr.pop(arr.index(max(arr)))
        if int(d)==0:
            return "0"
        return d
