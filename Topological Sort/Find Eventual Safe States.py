class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dictr = {}
        arr  = [0]*len(graph)
        output = []
        visited = set()
        

        def dfs(k):
            if k in dictr: return dictr[k]
            for i in (graph[k]):
                # print(i)
                if i in visited and i in dictr and dictr[i]==False: 
                    # visited.add(k)
                    # dictr[k] = False
                    return False
                if i in visited and i not in dictr: 
                    return False
                
                visited.add(i)
                M = dfs(i)
                
                dictr[i] = M
                if M == False: 
                    # visited.add(k)
                    # dictr[k] = False
                    return False
            output.append(k)
            # visited.add(k)
            # dictr[k] = True
            return True
        
         
        
        for l in range(len(graph)):
            if l not in visited:
                visited.add(l)
                x = dfs(l)
                dictr[l] = x
        # print(dictr)             
                    
        output.sort()
        return output
