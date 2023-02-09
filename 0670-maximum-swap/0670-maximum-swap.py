class Solution:
    def maximumSwap(self, num: int) -> int:
        high_digit = high_pos = 0
        low_digit = low_pos = 0
        cur_high_digit, cur_high_pos = -1, 0
        pos = 1
        
        res = num
        while num: 
            digit = num % 10
            if digit > cur_high_digit:
                cur_high_digit, cur_high_pos = digit, pos
            elif digit < cur_high_digit:
                high_digit, high_pos = cur_high_digit, cur_high_pos
                low_digit, low_pos = digit, pos
            
            pos *= 10
            num //= 10
        res += high_digit*(low_pos - high_pos) + low_digit*(high_pos - low_pos)
        return res