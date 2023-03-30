class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @lru_cache
        def dp(s1, s2):
            if len(s2) == 1:
                return s1[0] == s2[0]
            answer = False
            s1d = Counter()
            s2d = Counter()
            s2t = Counter()
            for i in range(len(s2)-1):
                s1d[s1[i]] += 1
                s2d[s2[i]] += 1
                s2t[s2[len(s2)-i-1]] += 1
                if s1d == s2d:
                    answer = answer or (dp(s1[:i+1], s2[:i+1]) and dp(s1[i+1:], s2[i+1:]))
                if s1d == s2t:
                    answer = answer or (dp(s1[:i+1], s2[len(s2)- (i+1):]) and dp(s1[i+1:], s2[:len(s2)- (i+1)]))
            return answer
        
        return dp(s1,s2)