def ai(nums,s,e)->int:
    if s==e:
        return nums[s]
    else:
        return max(nums[s]-ai(nums,s+1,e), nums[e]-ai(nums,s,e-1))
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if ai(nums,0,len(nums)-1)>=0:
            return True
        else:
            return False
