class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        su = 0
        test = True
        ans = 1
        while True:
            if test:    
                su += q
                if su%p == 0:
                    if (su/p)%2 == 0: return 0
                    return 1
                test = False
            else:
                su += q
                if su % p == 0:
                    return 2
                test = True
