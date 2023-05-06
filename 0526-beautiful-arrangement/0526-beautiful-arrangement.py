class Solution:
    def countArrangement(self, n: int) -> int:
        arr = [0] * n
        def back(i):
            if i == n + 1:
                return 1
            
            ans = 0
            for index in range(1,n+1):
                if (index % i == 0 or i % index == 0) and arr[index - 1] == 0:
                    arr[index - 1] = 1
                    ans += back(i+1)
                    arr[index - 1] = 0
            return ans
        return back(1)