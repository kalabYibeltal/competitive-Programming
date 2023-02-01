class Solution:
    def numberToWords(self, num: int) -> str:
        Ones = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
                6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',0:''}
        Tens_dig = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
                    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',0:''}
        Tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 
                6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety',0:''}
        Hundred = 'Hundred'
        Thousand = 'Thousand'
        Million = 'Million'
        Billion = 'Billion'
        
        
        def make(i):
            if i == 10:
                n = int(num/10**9)
                return " " + Ones[n] + " " + Billion + make(i-1)
            if i == 9:
                n = int(num/10**8) - (int(num/10**9) * 10)
                if n == 0: return Ones[0] + make(i-1)
                return " " + Ones[n] + " " + Hundred + make(i-1) 
            if i == 8:
                n = int(num/10**7) - (int(num/10**8) *10)
                t = int(num/10**6) - (int(num/10**7) *10)
                if n == 0:return  Ones[0] + make(i-1)
                if n == 1:
                    return " " +Tens_dig[n*10+t] + " " + Million + make(i-2)
                else:
                    if t == 0: return " " + Tens[n] +  " " + Million + make(i-2)
                    return " " +Tens[n] + " " + Ones[t] + " " + Million+  make(i-2)
            
            if i == 7:
                n = int(num/10**6) - (int(num/10**7) * 10)
                if n == 0:
                    if int(num/10**7) - (int(num/10**8) *10) > 0 or int(num/10**8) - (int(num/10**9) * 10) >0:
                        return Ones[0] + " " + Million + make(i-1)
                    return Ones[0] + make(i-1)
                return " " +Ones[n] + " " + Million + make(i-1)
            
            if i == 6:
                n = int(num/10**5) -(int(num/10**6) * 10)
                if n == 0:return Ones[0] + make(i-1)
                return " " +Ones[n] + " " + Hundred +  make(i-1) 
            if i == 5:
                n = int(num/10**4) - (int(num/10**5) * 10)
                t = int(num/10**3) - (int(num/10**4) * 10)
                if n == 0:return  Ones[0] + make(i-1)
                if n == 1:
                    print(n,t)
                    return " " +Tens_dig[n*10+t] + " " + Thousand + make(i-2)
                else:
                    if t == 0: return " " + Tens[n] +  " " + Thousand + make(i-2)
                    return " " +Tens[n] + " " + Ones[t] + " " + Thousand+  make(i-2)
        
            if i == 4:
                n = int(num/10**3) - (int(num/10**4) * 10)
                if n == 0: 
                    if int(num/10**4) - (int(num/10**5) * 10) > 0 or int(num/10**5) -(int(num/10**6) * 10) >0:
                        return Ones[0] + " " + Thousand + make(i-1)
                    return Ones[0] + make(i-1)
                return " " + Ones[n] + " " + Thousand +  make(i-1)
            
            if i == 3:
                n = int(num/10**2) - (int(num/10**3) * 10)
                if n == 0:return Ones[0] + make(i-1)
                return " " + Ones[n] + " " + Hundred +  make(i-1) 
            if i == 2:
                n = int(num/10) - (int(num/100) * 10)
                t = num - (int(num/10) *10 )
                if n == 0: return Ones[0] + make(i-1)
                if n == 1:
                    return " " + Tens_dig[n*10+t]
                else:
                    if t == 0: return " " + Tens[n]
                    return " " + Tens[n] + " " +Ones[t]
            if i == 1:
                n = num - (int(num/10) * 10)
                if n == 0: return Ones[0] 
                return " " + Ones[n] 
        
        if num == 0: return "Zero"
        s = len(str(num))
        return make(s)[1:]
                
                
                
                
             