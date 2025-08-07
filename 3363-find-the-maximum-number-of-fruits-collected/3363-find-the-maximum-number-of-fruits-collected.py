class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N=len(fruits)
        diag = 0
        for i in range(N):
            diag += fruits[i][i]
        fs = [[0 for _ in range(N)] for _ in range(N)]
        fs[0][-1] = fruits[0][-1]
        for i in range(1,N):
            for j in range(max(i+1,N-i-1),N):
                fs[i][j] = max(fs[i-1][j],fs[i-1][j-1],fs[i-1][min(N-1,j+1)])+fruits[i][j]
        fs[-1][0]=fruits[-1][0]
        for j in range(1,N):
            for i in range(max(j+1,N-j-1),N):
                fs[i][j] = max(fs[i-1][j-1], fs[i][j-1], fs[min(i+1,N-1)][j-1])+fruits[i][j]
        return fs[-1][-2]+fs[-2][-1]+diag
        
