class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        d={1<<i:i for i in range(1,7)}
        s=(1<<7) - 1
        for t,b in zip(tops,bottoms):
            s&=(1<<t)|(1<<b)
        if not s:
            return -1
        N=len(tops)
        w=s&(-s)
        tg = d[w]
        tct=0
        for t in tops:
            if t==tg:
                tct+=1

        bct=0
        for b in bottoms:
            if b==tg:
                bct+=1

        return N-max(bct,tct)