class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)-1
        m=len(mat[0])-1
        return [mat[i][s-i] for s in range(n+m+1) for i in range(max(0,s-m),min(n+1,s+1))[::1 if s%2 else -1]]