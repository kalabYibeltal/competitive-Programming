class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        flowers.sort()
        
        def right_finder(val):
            left = 0
            right = len(persons) - 1
            ans = 0
            if val < persons[0]:
                return -1
            while left <= right:
                mid = (left + right) // 2
               
                if val >= persons[mid]:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
            
        
        people = defaultdict(list)
        
        for i in range(len(persons)):
            
            people[persons[i]].append(i)
            
        persons.sort()
        
        prefix_persons = [0] * (len(persons) + 1)
        
        left = 0
        
        for start, end in flowers:
            
            while start > persons[left]:
                left += 1
                if left == len(persons):
                    break
            
            if left == len(persons):
                    break
            
            
            prefix_persons[left] += 1
            
            prefix_persons[right_finder(end) + 1] -= 1
            
        for i in range(1,len(prefix_persons)):
            prefix_persons[i] += prefix_persons[i-1]
        
         
        out = [0] * len(persons)
        
        
        dic = defaultdict(list)
        for index, val in enumerate(persons):
            dic[val].append(index)
        
        for key in people:
            for index2, index in enumerate(people[key]):
                out[index] = prefix_persons[dic[key][index2]]

        return out
            
            
            
            
        
        
        
        