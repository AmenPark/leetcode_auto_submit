class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        N=len(values)
        dp = [[1000000000 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][(i+1)%N] = 0
        for width in range(2,N):
            for i in range(N):
                j=(i+width)
                jn = j%N
                for k in range(i+1, j):
                    kn = k%N
                    dp[i][jn] = min(dp[i][jn], dp[i][kn]+dp[kn][jn]+values[i]*values[kn]*values[jn])

        return min([dp[i][i-1] for i in range(N)])