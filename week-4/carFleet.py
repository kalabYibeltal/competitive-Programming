class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dictr={}
        i=0
        fleet=1
        while i<len(speed):
            dictr[position[i]]=speed[i]
            i+=1
        dic=sorted(dictr)
        i=len(speed)-2
        t=(target-dic[len(speed)-1])/dictr[dic[len(speed)-1]]
        while i>-1:
            x=dic[i]
            xa=dictr[dic[i]]
            y=dic[i-1]
            ya=dictr[dic[i-1]]
            
            if (target-x)/xa>t:
                fleet+=1
                t=(target-dic[i])/dictr[dic[i]]
            i=i-1
     
        return fleet
