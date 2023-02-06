class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        dictr = {}
        for index,item in enumerate(words):
            if item in dictr: continue
            dictr [item] = []
            for i in range(index+1,len(words)):
                if len(words[i]) -1 > len(item): break
                elif len(words[i]) - 1 == len(item):
                    test = True
                    test2 = True
                    j = 0
                    while j < len(item):
                        if not test:
                            if item[j] != words[i][j+1]: 
                                test2 = False
                                break
                        elif item[j] != words[i][j]: 
                            test = False
                            j = j - 1
                        j += 1
                    
                    if test2: dictr[item].append(i)
                    # if item == 'x': print(words[i],test2)
        
#         print(words)
#         print(dictr['x'])
        ans = {}
        
        def dfs(word):
            if dictr[word] == []: return 1
            if word in ans: return ans[word]
            maxx = 0
            for i in dictr[word]:
                x = dfs(words[i])
                if x > maxx: maxx = x
            
            ans[word] = maxx
            return maxx + 1
                          
#         print(dfs("x"))
#         print(ans)
        maxxy= 0
        for j in words:
            x = dfs(j)
            if x > maxxy: maxxy = x
                
        return maxxy
            