class Solution:
    def bestClosingTime(self, customers: str) -> int:
        Ys = Counter(customers)['Y']
        answer = Ys
        sol = 0
        Ns = 0
        for i in range(len(customers)):
            l = customers[i]
            if l == 'N':Ns += 1
            else: Ys -= 1
            
            if  Ys + Ns < answer:
                answer = Ys + Ns
                sol = i + 1
        
        return sol
        