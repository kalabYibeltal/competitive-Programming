class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 =[]
        s= ""
        for i in version1:
            if i == '.': 
                if s == "": v1.append(int(0))
                else: v1.append(int(s))
                s = ""
            elif (s == "" and i == '0'): continue
            else: s = s + i
        if s == "": v1.append(int(0))
        else: v1.append(int(s))
                    
        v2 =[]
        s= ""
        for i in version2:
            if i == '.': 
                if s == "": v2.append(int(0))
                else: v2.append(int(s))
                s = ""
            elif (s == "" and i == '0'): continue
            else: s = s + i
        if s == "": v2.append(int(0))
        else: v2.append(int(s))
                    
        
        m = min(len(v1),len(v2))
        i = 0
        while i < m:
            if v1[i] > v2[i]: return 1
            elif v2[i] > v1[i]: return -1
            i += 1
        
        if len(v1) == len(v2): return 0
        if len(v1) > len(v2) and max(v1[len(v2):len(v1)]) > 0: return 1
        if len(v2) > len(v1) and max(v2[len(v1):len(v2)]) > 0: return -1
        return 0
