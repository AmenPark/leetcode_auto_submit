class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {0:1}
        ans = 0
        i=0
        while i<=high:
            if i not in dp:
                i+=1
                continue
            dp[i+one] = dp.get(i+one,0)+ dp[i]
            dp[i+zero] = dp.get(i+zero,0)+ dp[i]
            if i>=low:
                ans+=dp[i]
            i+=1
        return ans % (10**9 + 7)