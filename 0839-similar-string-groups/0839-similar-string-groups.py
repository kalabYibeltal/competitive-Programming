class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = []
        rank = []
        for i in range(len(strs)):
            parent.append(i)
            rank.append(1)
            
        def findparent(node):
            if parent[node] == node:
                return node
            parent[node] = findparent(parent[node])
            return parent[node]
            
        def union(node1, node2):
            pa = findparent(node1)
            pb = findparent(node2)
            if pa == pb: return 
            if rank[pa] >= rank[pb]:
                pa, pb = pb, pa

            parent[pa] = pb
            rank[pb] += rank[pa]
        
        def check(str1, str2):
            count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count += 1
                    if count > 2:
                        return False
            
            return True
        
   
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if check(strs[i], strs[j]):
                    union(i,j)
        
        parents = set()
        for i in range(len(strs)):
            x = findparent(i)
            if x not in parents:
                parents.add(x)
        
        return len(parents)
        
        
        