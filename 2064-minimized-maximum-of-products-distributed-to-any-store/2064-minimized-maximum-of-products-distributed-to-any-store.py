class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def getvalue(m):
            rt=0
            for q in quantities:
                rt += ((q-1)//m) + 1
            return rt
        s=sum(quantities)
        if getvalue(1)<=n:
            return 1
        l=1
        r=10**10
        while l<r-1:
            m=(l+r)//2
            if getvalue(m) <=n:
                r=m
            else:
                l=m
        return r

