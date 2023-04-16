class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        arr = [defaultdict(int) for i in range(len(words[0]))] 
        
        for i in range(len(words[0])):
            for j in range(len(words)):
                arr[i][words[j][i]] += 1
        
        
        @lru_cache(None)
        def dp(indexw, indext):
            if indext == len(target):
                return 1
            if indexw == len(words[0]):
                return 0
            
            return arr[indexw][target[indext]] * dp(indexw + 1, indext +1) +  dp(indexw + 1, indext)
        
        return dp(0,0) % 1000000007 
            
            
            