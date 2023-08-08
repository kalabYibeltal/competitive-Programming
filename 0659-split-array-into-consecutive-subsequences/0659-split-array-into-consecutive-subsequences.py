class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        answer = []
        heappush(heap, [nums[0], 1])
        
        for i in range(1,len(nums)):
            if not heap:
                heappush(heap, [nums[i], 1])
                continue
            val, leng = heappop(heap)
            # print(val, leng, i)
            if nums[i] == val:
                heappush(heap, [val, leng])
                heappush(heap, [nums[i], 1])
                continue
            elif nums[i] > val + 1:
                answer.append([val, leng])
                while heap:
                    val, leng = heappop(heap)
                    if nums[i] == val + 1:
                        break
                    else:
                        answer.append([val, leng])
                        
                if not heap and not (nums[i] == val + 1):
                    heappush(heap, [nums[i], 1]) 
                    continue
                    
            heappush(heap, [val + 1, leng + 1])
        
        # print(heap, answer)
        
        for val, leng in heap:
            if leng < 3:
                return False
        for val, leng in answer:
            if leng < 3:
                return False
        return True