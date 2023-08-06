class LUPrefix:

    def __init__(self, n: int):
        self.visited = set()
        self.max = 0
    def upload(self, video: int) -> None:
        self.visited.add(video)

    def longest(self) -> int:
        for i in range(self.max, 1000000):
            if (self.max + 1) in self.visited:
                self.max += 1
            else:
                break
        return self.max

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()