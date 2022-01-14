
def cal(x,n)->float:
    if n==1:
        return x
    elif x==0.0:
        return 0.0
    return x*cal(x,n-1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
            
        if x==1:
            return 1
        elif n==0:
            return 1
        elif abs(n)>1000:
            r=abs(n)%1000
            y=int(abs(n)/1000)  
            if y>1000:
                t=y%1000
                v=int(y/1000)
                if n<0:
                    o=(cal(((cal(cal(x,1000),v))*cal(x,t)),1000)) *cal(x,r)
                    return 1/o
                return (cal(((cal(cal(x,1000),v))*cal(x,t)),1000)) *cal(x,r)    
            elif n<0:
                z=cal(x,1000)
                l=(cal(z,y)*cal(x,r))
                return 1/l
            return (cal(cal(x,1000),y)*cal(x,r))
        
        elif n<0:
            return 1/cal(x,abs(n))
        return cal(x,n)
