class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        parts = set()
        arr = []
        for c in words:
            if c == "":continue
            parts.add(c)
        
        dictr = {}
        def dfs(l,r,w):
            if (l,r) in dictr: return dictr[(l,r)]
            if l == 0 and r == len(w)-1: return False
            if r == len(w)-1 and w[l:r+1] in parts: return  True
            while not(w[l:r+1] in parts):
                if r == len(w)-1 and not(w[l:r+1] in parts): return False
                r += 1
            
            # print(w[l:r+1])
            if l == 0 and r == len(w)-1: return False
            if r == len(w)-1 and w[l:r+1] in parts: return  True
            dictr[(l,r)] = dfs(r+1,r+1,w) or dfs(l,r+1,w)
            return dictr[(l,r)]
            
        
        
        
        # print(dfs(0,0,"catrtcat"))
        for c in words:
            valid = True
            dictr = {}
            if c == "":continue
            if dfs(0,0,c): arr.append(c)
                
                
        return arr
