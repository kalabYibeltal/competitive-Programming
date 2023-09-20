class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        sol = []
        for num in arr:
            sol.append(num)
        
        solution = 0
        while len(sol) > 1:
            index = 0
            tot = inf
            for i in range(len(sol)-1):
                if sol[i] * sol[i+1] < tot:
                    tot = sol[i] * sol[i+1]
                    index = i
            solution += sol[index]*sol[index+1]
            sol = sol[:index] + [max(sol[index],sol[index+1])] + sol[index+2:]
            
            
        return solution
                
                
                
                
                
                
            
            
            
        