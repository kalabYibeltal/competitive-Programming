class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque([(0, 0, 1)])
        while queue:
            moves, pos, val = queue.popleft()
            if pos == target:
                return moves
            
            queue.append((moves + 1, pos + val, 2 * val))
            if (pos + val > target and val > 0) or (pos + val < target and val < 0):
                queue.append((moves + 1, pos, -1 if val > 0 else 1))