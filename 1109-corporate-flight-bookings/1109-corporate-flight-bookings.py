class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        out =  [0] * (n+1)
        for x, y , b in bookings:
            out[y] += b
            out[x-1] -= b
        
        for i in range(len(out)-2,0,-1):
            out[i] = out[i] + out[i+1]
        
        return out[1:]
            
            