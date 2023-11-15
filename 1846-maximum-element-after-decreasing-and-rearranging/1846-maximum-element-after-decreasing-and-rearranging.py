class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        sol = 1
        for index, num in enumerate(arr):
            if index == 0:
                arr[0] = 1
            
            elif num > arr[index - 1]:
                sol = arr[index - 1] + 1
                arr[index] = sol
            
        return sol
                
            