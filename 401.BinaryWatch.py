class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def dfs(LEDS, idx, hrs, mins, n):
            # base cases
            if hrs >= 12 or mins >= 60:
                return
            if n == 0:
                time = str(hrs) + ":" + "0"*(mins<10) + str(mins)
                result.append(time)
                return

            if idx < len(LEDS):
                if idx <= 3:  # handle hours
                    dfs(LEDS, idx+1, hrs + LEDS[idx], mins, n-1)
                else:  # handle minutes
                    dfs(LEDS, idx+1, hrs, mins + LEDS[idx], n-1)
                dfs(LEDS, idx+1, hrs, mins, n)
        result = []
        LEDS = [
            8, 4, 2, 1,  # top row of watch
            32, 16, 8, 4, 2, 1 # bottom row of watch
        ]
        dfs(LEDS, 0, 0, 0, num)
        
        return result
        
        #my dumb answer
        H = [1,2,4,8]
        M = [1,2,4,8,16,32]
        output = []
        def back(ons,hour, hi, minute, mi):
            if ons == 0:
                if hour < 12 and minute < 60:
                    output.append(str(hour) + ":" + str(minute).rjust(2, '0'))
                return 
            
            for m in range(mi, 6):
                back(ons-1, hour, hi , minute + M[m], m + 1)
                    
            for h in range(hi, 4):
                back(ons-1, hour + H[h], h + 1, minute, mi)
            
            
        
        back(turnedOn, 0 ,0, 0, 0)
        return set(output)
    
 
