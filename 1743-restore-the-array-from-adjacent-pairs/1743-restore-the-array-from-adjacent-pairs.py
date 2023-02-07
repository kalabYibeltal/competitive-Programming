class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        visited={}
        a1={}
        for i in adjacentPairs:
            if i[0] not in a1:
                a1[i[0]]=[]
            if i[1] not in a1:
                a1[i[1]]=[]
            a1[i[0]].append(i[1])
            a1[i[1]].append(i[0])
      
        e=adjacentPairs[0][0]
        for i in a1:
            if len(a1[i])==1:
                e=i
        
        queue=[e]
        output=[]
        visited[e]=1
        while(len(queue)>0):
            x=queue.pop(0)
            output.append(x)
            for i in a1[x]:
                if i not in visited:
                    visited[i]=1
                    queue.append(i)
        return output