class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        M = len(matrix[0])
        rf = False
        cf = False
        for j in range(M):
            if matrix[0][j] == 0:
                cf = True
                break
        for i in range(N):
            if matrix[i][0] == 0:
                rf = True
                break
        
        for i in range(1,N):
            for j in range(1,M):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,N):
            if matrix[i][0] == 0:
                for j in range(1,M):
                    matrix[i][j]=0
        for j in range(1,M):
            if matrix[0][j] == 0:
                for i in range(1,N):
                    matrix[i][j] = 0
        
        if cf:
            for j in range(M):
                matrix[0][j]=0
        if rf:
            for i in range(N):
                matrix[i][0] = 0