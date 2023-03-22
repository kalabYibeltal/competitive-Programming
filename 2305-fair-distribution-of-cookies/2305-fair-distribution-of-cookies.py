class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = inf
        arr = [0] * k
        def back(index):
            nonlocal ans
            if index == len(cookies):
                ans = min(ans, max(arr))
                return
            for i in range(k):
                arr[i] += cookies[index]
                if arr[i] < ans:
                    back(index + 1)
                arr[i] -= cookies[index]
        
        
        back(0)
        return ans