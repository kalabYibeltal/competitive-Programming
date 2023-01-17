class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        count = set()
        # nums = set(nums)
        for n in nums:
            # if n in visited: continue
            if dic[n-k] > 0:
                count.add((n-k, n))
            if dic[n+k] > 0:
                count.add((n, n+k))
            
            dic[n] +=1
        
        print(count)
        return len(count)