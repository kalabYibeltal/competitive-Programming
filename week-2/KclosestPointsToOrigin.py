class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        i=0
        count=0
        arr=[]
        maxn=0
        max2=0
        l=0
        dictr={}
        while(i<len(points)):
            length=((points[i][0])**2)+((points[i][1])**2)
            if length in dictr:
                dictr[length].append(points[i])
            else:
                dictr[length]=[points[i]]
            i+=1
        dictor=sorted(dictr)
        for c in dictor:
            arr.extend(dictr[c])
            if len(arr)==k:
                return arr
        return arr
