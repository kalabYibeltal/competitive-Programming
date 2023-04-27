class Solution:
    def bulbSwitch(self, n: int) -> int:
        ## georg answer
        int(pow(n,0.5))
        ### my answer
        if n == 0: return 0
        counter = 3
        adder = 3
        num = 1
        while counter < n:
            adder += 2
            counter += adder
            num += 1
            
        return num
    
    