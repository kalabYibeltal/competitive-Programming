def fibb(n)->int:
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibb(n-1) + fibb(n-2)
class Solution:
    def fib(self, n: int) -> int:
        return fibb(n)
