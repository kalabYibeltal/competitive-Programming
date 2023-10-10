class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
#         @lru_cache(None)
#         def dp(index, prev, turn, sign): 
#             if index == len(rating): return 0
            
#             if turn == 3:
#                 return ((rating[index] > rating[prev] and sign == 1) or (rating[index] < rating[prev] and sign == 0)) + dp(index +1, prev, turn, sign)
            
        
#             if sign == 1:
#                 ans = 0
#                 if rating[index] > rating[prev]:
#                     ans = dp(index+1, index, turn + 1, sign)
                
#                 return ans + dp(index +1, prev, turn, sign)
    
#             ans = 0
#             if rating[index] < rating[prev]:
#                 ans = dp(index+1, index, turn + 1, sign)

#             return ans + dp(index +1, prev, turn, sign)
        
        
#         ans = 0
#         for i in range(len(rating)):
#             ans += dp(i,i,2,0) + dp(i,i,2,1)
        
        # return ans
        
        more = [0] * len(rating)
        less = [0] * len(rating)
        answer = [0] * len(rating)

        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                if rating[j] > rating[i]:
                    more[i] += 1
                else:
                    less[i] += 1
        
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                if rating[j] > rating[i]:
                    answer[i] += more[j]
                else:
                    answer[i] += less[j]
        
        return sum(answer)
        
        
        
        
        
        
        
                
                
                
                
        