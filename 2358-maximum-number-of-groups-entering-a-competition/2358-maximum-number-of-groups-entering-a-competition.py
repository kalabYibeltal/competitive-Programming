class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        x = 1
        count = 0
        while n - x  >= 0:
            n -= x
            x += 1
            count += 1
        
        return count