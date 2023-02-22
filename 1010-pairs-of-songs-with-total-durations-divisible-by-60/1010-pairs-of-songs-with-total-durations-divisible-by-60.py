class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs, target = 0, 60
        rem_count = defaultdict(int)
        
        for t in time:
            rem = t % target
            pairs += rem_count[rem]
            if rem == 0:
                rem_count[0] += 1
            else:
                rem_count[target - rem] += 1        
        
        return pairs