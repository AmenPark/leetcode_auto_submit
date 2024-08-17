class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = iter(points)
        scores=next(rows)
        N=len(scores)
        lmax = [0]*N
        rmax = [0]*N
        for row in rows:
            lval = scores[0]-(N-1)
            rval = scores[-1]-(N-1)
            for i in range(N):
                lmax[i] = max(lval, scores[i]-(N-1-i))
                rmax[-1-i] = max(rval, scores[-1-i]-(N-1-i))
                lval = lmax[i]
                rval = rmax[-1-i]
            for i in range(N):
                scores[i] = max(lmax[i]+(N-i-1), rmax[i]+(i)) +row[i]
        return max(scores)

