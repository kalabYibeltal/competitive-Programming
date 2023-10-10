class Solution:
    def numSplits(self, s: str) -> int:
        
        total = set(s)
        total_C = Counter(s)
        prefix = set()
        count = 0
        
        for i in range(len(s)-1):
            total_C[s[i]] -= 1
            if total_C[s[i]] == 0:
                total.remove(s[i])
            
            prefix.add(s[i])
            
            count += (len(prefix) == len(total))
                
        
        return count