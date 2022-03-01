class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        boll=False
        while left <= right:
            mid = (left+right)//2
            if matrix[mid][0] > target:
                right = mid-1
            elif matrix[mid][-1] < target:
                left= mid+1
            else:
                boll=True
                break
        left=0
        right=len(matrix[0])-1
        booll=False
        if boll:
            while left<=right:
                mid2 = (left+right)//2
                if matrix[mid][mid2] > target:
                    right = mid2-1
                elif matrix[mid][mid2] < target:
                    left= mid2 + 1
                else:
                    booll=True
                    break
        return booll
        
