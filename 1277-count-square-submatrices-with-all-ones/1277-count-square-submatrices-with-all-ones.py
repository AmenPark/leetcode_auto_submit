class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        N=len(matrix)
        M=len(matrix[0])
        ans += matrix[0][0]
        for i in range(1,N):
            ans += matrix[i][0]
        for j in range(1,M):
            ans += matrix[0][j]
        print(ans)
        for i in range(1,N):
            for j in range(1,M):
                if matrix[i][j]==1:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])+1
                    ans += matrix[i][j]
        return ans