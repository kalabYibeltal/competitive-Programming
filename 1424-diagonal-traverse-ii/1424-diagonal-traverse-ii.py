class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        heap = []
        
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                heap.append([row+col, col, nums[row][col]])
            
        
        return [x for y,z,x in sorted(heap)]
        
            
            