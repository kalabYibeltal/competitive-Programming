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
            
            new_sol = []
            i = 0
            while i < len(sol):
                if i == index:
                    new_sol.append(max(sol[i],sol[i+1]))
                    solution += sol[i]*sol[i+1]
                    i += 2  
                else:
                    new_sol.append(sol[i])
                    i += 1
            
            sol = new_sol
            
        return solution
                
                
                
                
                
                
            
            
            
        