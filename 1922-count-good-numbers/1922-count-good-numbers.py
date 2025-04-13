class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9 + 7
        a=n//2
        b=(n+1)//2
        return (pow(4,a,mod) * pow(5,b,mod))%mod