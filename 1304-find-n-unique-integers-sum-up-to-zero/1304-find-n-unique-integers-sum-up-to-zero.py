class Solution:
    def sumZero(self, n: int) -> List[int]:
        values = []
        [values.append(i) for i in range(1, n+1)]
        values[-1] = -sum(values[:-1])
        return values