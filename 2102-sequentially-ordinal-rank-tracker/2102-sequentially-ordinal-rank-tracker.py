from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.array = SortedList()
        self.count = 0

    def add(self, name: str, score: int) -> None:
        self.array.add([-score,name])

    def get(self) -> str:
        val, name = self.array[self.count]
        self.count += 1
        return name

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()