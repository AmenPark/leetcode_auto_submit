class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minrow = {min(m) for m in matrix}
        maxcol = {max([matrix[j][i] for j in range(len(matrix))])for i in range(len(matrix[0]))}
        ans = []
        for mr in minrow:
            if mr in maxcol:
                ans.append(mr)
        return ans