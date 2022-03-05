import collections
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
    
        que= collections.deque([start])
        visited=set()
        while que:
            cur=que.popleft()
            visited.add(cur)
            if arr[cur]==0:
                return True
            if cur-arr[cur] not in visited and cur-arr[cur]>=0:
                que.append(cur-arr[cur])
                visited.add(cur-arr[cur])
            if cur+arr[cur] not in visited and cur+arr[cur] < len(arr):
                que.append(cur+arr[cur])
                visited.add(cur+arr[cur])
        return False
