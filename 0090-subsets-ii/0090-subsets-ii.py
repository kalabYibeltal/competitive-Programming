class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        answer = []
        track = []
        visited = set()
        
        def back(index):
            if index == len(nums):
                if tuple(track) not in visited:
                    answer.append(track[:])
                    visited.add(tuple(track))
                return 
            track.append(nums[index])
            back(index + 1)
            track.pop()
            back(index + 1)
        
        back(0)
        return answer