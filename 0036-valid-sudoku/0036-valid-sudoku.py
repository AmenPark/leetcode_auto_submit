class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            d = set()
            for v in row:
                if v==".":
                    continue
                if v in d:
                    return False
                d.add(v)
        for i in range(9):
            d = set()
            for j in range(9):
                v=board[j][i]
                if v==".":
                    continue
                if v in d:
                    return False
                d.add(v)
        for xi in range(0,9,3):
            for yi in range(0,9,3):
                d=set()
                for i in range(9):
                    v=board[xi+i%3][yi+i//3]
                    if v==".":
                        continue
                    if v in d:
                        return False
                    d.add(v)
        return True