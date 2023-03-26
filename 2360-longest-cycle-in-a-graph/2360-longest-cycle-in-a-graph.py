class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        leng = -1
        
        visited = {}
        path = {}
        def rec(index,val):
            if edges[index] in visited:
                visited[index] = visited[edges[index]]
                return visited[edges[index]]
            if edges[index] in path:
                visited[index] = val - path[edges[index]] + 1
                return visited[index]
            
            elif edges[index] == -1:
                visited[index] = - 1
                return visited[index]
            
            else:
                path[index] = val
                visited[index] = rec(edges[index], val + 1)
                del path[index]
            
            return visited[index]
        
        for i in range(len(edges)):
            leng = max(leng, rec(i,1))
        
        return leng