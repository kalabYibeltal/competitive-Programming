class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        negoarr = []
        negcarr = []
        posoarr = []
        poscarr = []
        
        negop = negcp = posop = poscp = 0
        
        for o, c, dirr in shifts: 
            if dirr == 0:
                negoarr.append(o)
                negcarr.append(c)
            else:
                posoarr.append(o)
                poscarr.append(c)
        
        negoarr.sort()
        negcarr.sort()
        posoarr.sort()
        poscarr.sort()
        
        answer = ""
        
        for l in range(len(s)):
            while negop < len(negoarr) and negoarr[negop] <= l:
                negop += 1
            
            while negcp < len(negcarr) and negcarr[negcp] < l:
                negcp += 1
            
            while posop < len(posoarr) and posoarr[posop] <= l:
                posop += 1
            
            while poscp < len(poscarr) and poscarr[poscp] < l:
                poscp += 1
            
            answer += chr( ((ord(s[l]) - ord('a') + (posop - poscp) - (negop - negcp) ) % 26) +  ord('a'))
        
        return answer
            