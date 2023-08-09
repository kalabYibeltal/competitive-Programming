class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        dic = defaultdict(int)
        # answer = 
        nums.sort()
        
        for index in range(len(nums)):
            num = nums[index]
         
            if (num % space) in dic:
                dic[num % space][0] += 1
            else:
                dic[num % space] = [1, -num]
                
                
#             if -num in dic:
#                 dic[-num] += 1
#             elif -(num - space) not in dic:
#                 dic[-num] = 1
#                 parent[num] = num
#             else:
#                 parent[num] = parent[num - space]
#                 dic[-parent[num]] += 1
       
        # print(dic)
        answer = max([dic[key] for key in dic])
        print(answer)
        return answer[1] * -1
    
    