class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = defaultdict(list)
        dictr = defaultdict(set)
        for ind,i in enumerate(equations):
            dic[i[0]].append([i[1],values[ind]])
            dictr[i[0]].add((i[1],values[ind]))
            dic[i[1]].append([i[0],1/values[ind]])
            dictr[i[1]].add((i[0],1/values[ind]))
        
        
        def maper(num,let,i):
            dictr[i].add((let,num))
            for j in dic[let]:
                if j[0] not in visited:
                    visited.add(j[0])
                    maper(num*j[1],j[0],i)
        
        arr = []
        for i in dic:
            arr.append(i)
        for i in arr:
            
            visited = set()
            visited.add(i)
            for a in dic[i]:
                maper(a[1],a[0],i)
        
        # print(dictr)
        out = []
        for i in queries:
            if i[0] not in dictr or i[1] not in dictr:
                out.append(-1)
                continue
            if i[0] == i[1]:
                out.append(1)
                continue
            test = True
            for c in dictr[i[0]]:
                if c[0] == i[1]:
                    out.append(c[1])
                    test = False
                    break
            if test: out.append(-1)
            
        return out
            
 
                    
                
        
                
        