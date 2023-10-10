class Solution:
    def divisorGame(self, n: int) -> bool:
        
        @lru_cache(None)
        def dp(num, turn):
            if num == 1: return turn != 1
            if turn == 1:
                Bol = False 
                for i in range(1,num):
                    if num % i == 0:
                        Bol = Bol or dp(num -  i, 1-turn)
            
                return Bol
            
            Bol = True
            for i in range(1,num):
                if num % i == 0:
                    Bol = Bol and dp(num -  i, 1-turn)
            return Bol
        
        return dp(n,1)
            