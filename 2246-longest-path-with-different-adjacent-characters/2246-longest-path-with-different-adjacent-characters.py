class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for i in range(len(parent)):
            graph[parent[i]].append(i)
        
        # print(graph)
        
        total = 0
        def dfs(node):
            nonlocal total
            
            m1 = m2 = 0
            for nei in graph[node]:
                val = dfs(nei)
                if s[nei] != s[node]:
                    if val > m1:
                        m2 = m1
                        m1 = val
                    elif val > m2:
                        m2 = val
            
            total = max(total, m2 + 1 + m1)
            return m1 + 1
        
        dfs(0)
        return total
        
        
        
            
            
            
            