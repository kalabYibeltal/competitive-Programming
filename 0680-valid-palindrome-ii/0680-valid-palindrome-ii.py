class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return 
                left += 1
                right -= 1
            return True
    
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
            else:
                return is_pal(left + 1, right) or is_pal(left, right - 1)
        return True