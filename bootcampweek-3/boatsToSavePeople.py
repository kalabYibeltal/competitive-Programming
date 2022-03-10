class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        count=0
        for i in people:
            if i < limit:
                count+=1
        maxs=len(people)-count
        n=count
        i=0
        n=people[:count]
        while i < len(n):
            if i==len(n)-1: 
                maxs+=1
                break
            if n[i]+n[-1]<=limit:
                i+=1
                n.pop()
            else:
                maxs+=1
                n.pop()
        return maxs + (len(people)-maxs)//2
            
