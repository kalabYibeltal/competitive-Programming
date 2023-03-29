from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        s1 = SortedList()
        count = 0
        for i in range(len(nums1)):
            count += s1.bisect_right(nums1[i] - nums2[i] + diff)
            s1.add(nums1[i] - nums2[i])
        
        return count