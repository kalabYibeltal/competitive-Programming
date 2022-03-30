class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        maxx = len(numbers)-1
        minn = 0
        while True:
            if numbers[minn] + numbers[maxx] == target:
                return [minn+1,maxx+1]
            if numbers[minn] + numbers[maxx] > target:
                maxx -=1
            else:
                minn+=1
