class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0]*len(energy)
        N=len(energy)
        for i in range(N-1,-1,-1):
            if i+k < N:
                dp[i]=dp[i+k]+energy[i]
            else:
                dp[i]=energy[i]
        return max(dp)