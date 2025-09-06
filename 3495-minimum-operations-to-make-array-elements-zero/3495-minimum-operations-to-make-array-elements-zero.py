class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # 0->0, 1~3 -> 1, 4~15 -> 2, 16~63 -> 3,...
        def getOpsNum(l,r):
            if l==r:
                rt = 0
                while l:
                    l>>=2
                    rt+=1
                return rt
            else:
                return (ctOperNum(r) - ctOperNum(l-1)+1)//2
        def ctOperNum(n):
            if n<=0:
                return 0
            bd = 1
            rt=0
            i=1
            while True:
                nbd = bd<<2
                if nbd > n:
                    return rt + (i*(n-bd + 1))
                rt += i*(nbd - bd)
                i+=1
                bd=nbd
            return rt
        return sum(getOpsNum(*l) for l in queries)