class DataStream:

    def __init__(self, value: int, k: int):
        self.que = deque()
        self.count = 0
        self.value = value
        self.k = k
    def consec(self, num: int) -> bool:
        self.que.append(num)
        if num == self.value:
            self.count += 1
        if len(self.que) < self.k:
            return 
        if len(self.que) > self.k:
            if self.que[0] == self.value:
                self.count -= 1
            self.que.popleft()
        
        if self.count == self.k:
            return True
        return 


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)