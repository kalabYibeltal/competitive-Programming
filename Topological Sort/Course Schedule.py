class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      # using bfs
        dictr = {}
        arr = [0] * numCourses
        output = []
        for i in prerequisites:
            arr[i[0]] += 1
        for i in prerequisites:
            if i[1] in dictr:
                dictr[i[1]].append(i[0])
            else: dictr[i[1]]=[i[0]]
        # print(dictr)       
        que = collections.deque()
        for i in range(len(arr)):
            if arr[i] == 0: que.append(i)
        # print(que, arr)
        while que:
            val = que.popleft()
            output.append(val)
            # print(val)
            if val in dictr:
                for i in dictr[val]:
                    arr[i] -= 1
                    if arr[i]==0: que.append(i)
        # print(output)
        return len(output) == numCourses
