class RecentCounter:

    def __init__(self):
        self.req=0
        self.arr=[]
    def ping(self, t: int) -> int:
        self.arr.append(t)
        self.req+=1
        while self.arr[0]<(t-3000):
            self.arr.pop(0)
            self.req-=1
        return self.req


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
