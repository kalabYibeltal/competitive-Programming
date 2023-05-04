class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        arr = []
        for key in freq:
            if freq[key] == 1:
                arr.append(key)
        
        return arr