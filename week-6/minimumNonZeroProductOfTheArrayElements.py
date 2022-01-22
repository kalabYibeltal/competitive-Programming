class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        n=(pow(2,p)-2)
        return (pow(n,n//2,1000000007)*(n+1))%1000000007
