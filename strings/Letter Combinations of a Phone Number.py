class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
              # print("".join("sd"))
        def dig(n):
            if n == '2': return ['a','b','c']
            elif n == '3': return ['d','e','f']
            elif n == '4': return ['g','h','i']
            elif n == '5': return ['j','k','l']
            elif n == '6': return ['m','n','o']
            elif n == '7': return ['p','q','r','s']
            elif n == '8': return ['t','u','v']
            elif n == '9': return ['w','x','y','z']
        
        arr = []     
        if len(digits) == 0: return []
        if len(digits) == 1:
            ar2 = dig(digits[0])
            for j in ar2:
                arr.append(j)  
        elif len(digits) == 2:
            ar = dig(digits[0])
            ar2 = dig(digits[1])
            for i in ar:
                for j in ar2:
                    arr.append(i+j)  
        elif len(digits) == 3:
            ar = dig(digits[0])
            ar2 = dig(digits[1])
            ar3 = dig(digits[2])
            for i in ar:
                for j in ar2:
                    for k in ar3:
                        arr.append(i+j+k)
        elif len(digits) == 4:
            ar = dig(digits[0])
            ar2 = dig(digits[1])
            ar3 = dig(digits[2])
            ar4 = dig(digits[3])
            for i in ar:
                for j in ar2:
                    for k in ar3:
                        for l in ar4:
                            arr.append(i+j+k+l)

        return arr
            
#         def helper(self, s, i, digits):
#             if digits == "":
#                 return []
        
#             if i == len(digits):
#                 ans.append(s)
#                 return

#             for c in mapp[digits[i]]:
#                 s.append(c)
#                 helper(s,i+1, digits)
#                 s.pop()

   
#         mapp = {'2':"abc", 
#                     '3':"def", 
#                     '4':"ghi", 
#                     '5':"jkl", 
#                     '6':"mno", 
#                     '7':"pqrs", 
#                     '8':"tuv", 
#                     '9':"wxyz"}
         
#         ans = []
#         helper([], 0, digits)
        
#         return self.ans 
