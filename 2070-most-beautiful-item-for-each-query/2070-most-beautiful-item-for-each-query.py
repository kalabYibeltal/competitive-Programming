class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        output = [0] * len(queries)
        
        queries = [[queries[x], x] for x in range(len(queries))]
        queries.sort()
        
        ans = 0
        itr = 0
        
        for value, index in queries:
            
            while itr < len(items) and value >= items[itr][0]:
                ans = max(ans, items[itr][1])
                itr += 1
            
            output[index] = ans
        
        return output
        