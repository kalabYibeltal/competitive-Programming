class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if Counter(corridor)['S'] % 2 == 1 or Counter(corridor)['S'] == 0:
            return 0
        count = 0
        prev = 0
        
        answer = 1
    
        
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                count += 1
            
                if count % 2 == 1 and prev:
                    answer *= (i-prev) %1000000007
                
                else:
                    prev = i
            
        return answer%1000000007
                