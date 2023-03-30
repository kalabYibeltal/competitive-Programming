class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @lru_cache
        def dp(s1, s2):
            if len(s2) == 1:
                return s1[0] == s2[0]
            answer = False
            for i in range(len(s2)-1):
                if Counter(s1[:i+1]) == Counter(s2[:i+1]):
                    answer = answer or (dp(s1[:i+1], s2[:i+1]) and dp(s1[i+1:], s2[i+1:]))
                if Counter(s1[:i+1]) == Counter(s2[len(s2)- (i+1):]):
                    answer = answer or (dp(s1[:i+1], s2[len(s2)- (i+1):]) and dp(s1[i+1:], s2[:len(s2)- (i+1)]))
            return answer
        
        return dp(s1,s2)