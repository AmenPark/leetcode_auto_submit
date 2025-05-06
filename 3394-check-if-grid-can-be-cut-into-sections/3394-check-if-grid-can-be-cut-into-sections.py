class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        vers = []
        hors = []
        for sx,sy,ex,ey in rectangles:
            vers.append((sy, 1))
            vers.append((ey, -1))
            hors.append((sx,1))
            hors.append((ex,-1))
        vers.sort()
        hors.sort()
        depth = 0
        ct = 0
        for y,io in vers:
            depth += io
            if depth==0:
                ct+=1
        if ct>=3:
            return True
        ct=0
        depth=0
        for x,io in hors:
            depth+=io
            if depth==0:
                ct+=1
        if ct>=3:
            return True
        return False