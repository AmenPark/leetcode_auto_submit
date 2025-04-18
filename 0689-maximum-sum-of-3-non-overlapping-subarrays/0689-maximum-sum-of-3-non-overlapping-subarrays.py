class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N=len(nums)
        sumk = []
        s = sum(nums[:k])
        sumk.append(s)
        for i in range(N-k):
            s -= nums[i]
            s += nums[i+k]
            sumk.append(s)
        dp = [[(0,0),(0,0,0),(0,0,0,0)] for _ in range(N+1)]
        for i,num in enumerate(sumk):

            dp[i+k][2] = min((dp[i][1][0] - num,dp[i][1][1], dp[i][1][2],i), dp[i+k-1][2])
            dp[i+k][1] = min((dp[i][0][0]-num, dp[i][0][1],i), dp[i+k-1][1])
            dp[i+k][0]=min((-num,i), dp[i+k-1][0])
        _,*rt = dp[-1][-1]

        return rt        