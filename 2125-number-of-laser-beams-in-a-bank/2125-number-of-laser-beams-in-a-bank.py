class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        prev = 0
        for s in bank:
            val  = Counter(s)["1"]
            if val == 0: continue
            total += prev * val
            prev = val
        
        return total