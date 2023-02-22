class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        dic = {}
        for i in range(len(s)):
            if s[i] in dicts: 
                if t[i] in dictt and dictt[t[i]] == s[i]: 
                    dicts[s[i]][0].append(i)
                    dicts[s[i]][1].append(i)
                else: return 
            elif t[i] in dictt: return    
            else: 
                dictt[t[i]] = s[i]
                dicts[s[i]] = [[i],[i]]
                
        print(dicts)        
        return True
        
#         for i in range(len(t)):
#             if t[i] in dictt: dictt[t[i]].append(i)
#             else: dicts[t[i]] = [i]
        
#         for i in dicts