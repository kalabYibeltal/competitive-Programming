class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
            
        arr = []
        for i in range(len(scores)):
            arr.append([scores[i],ages[i]])
        arr.sort()
                        
   
        @lru_cache(None)
        def fn(i,maxs):
            
            if arr[i][1] >= maxs:
                if i == len(arr)-1: return arr[i][0]
                if arr[i][1] == maxs: return fn(i+1, maxs) + arr[i][0]
                return max((fn(i+1, arr[i][1]) + arr[i][0]),fn(i+1,maxs))
            
            if i==len(arr)-1: return 0
            return fn(i+1,maxs)
        
        return fn(0,0)
                    
        
        