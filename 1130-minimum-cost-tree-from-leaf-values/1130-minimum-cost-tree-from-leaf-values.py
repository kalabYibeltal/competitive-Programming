class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        sol = []
        for num in arr:
            sol.append([num,num])
        
        solution = 0
        while len(sol) > 1:
            index = 0
            tot = inf
            for i in range(len(sol)-1):
                if sol[i][1] * sol[i+1][1] < tot:
                    tot = sol[i][1] * sol[i+1][1]
                    index = i
            
            new_sol = []
            i = 0
            while i < len(sol):
                print(i)
                if i == index:
                    new_sol.append([sol[i][1]*sol[i+1][1], max(sol[i][1],sol[i+1][1]) ])
                    solution += sol[i][1]*sol[i+1][1]
                    i += 2
             
                
                else:
                    new_sol.append(sol[i])
                    i += 1
            
            sol = new_sol
            
        return solution
                
                
                
                
                
                
            
            
            
        