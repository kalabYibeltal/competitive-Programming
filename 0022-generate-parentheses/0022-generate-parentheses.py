class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        ans = []
   
        def make(i,count,total):
            if i == 2*n: 
                a = ''.join(str(x) for x in res)
                ans.append(a + ")")
                return
            if count > 0:
                res.append(")")
                make(i+1,count-1,total)
                res.pop()
            if total < n:
                res.append("(")
                make(i+1,count+1,total+1)
                res.pop()
        
        make(1,0,0)
        return ans
                
            
            