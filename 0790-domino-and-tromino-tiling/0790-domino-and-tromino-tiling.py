class Solution:
    def numTilings(self, n: int) -> int:
        dp = {0:1}
        odp = {}
        mod=10**9+7
        for i in range(1,n+1):
            dp[i] = dp.get(i-1,0) + dp.get(i-2,0) + odp.get(i-2,0) % mod
            odp[i] = dp.get(i-1,0)*2 + odp.get(i-1,0) % mod
        return dp[n] % mod