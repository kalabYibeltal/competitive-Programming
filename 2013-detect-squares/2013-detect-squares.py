class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: Counter())

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for pt in self.points[x]:
            if pt == y:
                continue
            for d in (y-pt, pt-y):
                ans += self.points[x-d][y] * self.points[x-d][pt] * self.points[x][pt]
        return ans