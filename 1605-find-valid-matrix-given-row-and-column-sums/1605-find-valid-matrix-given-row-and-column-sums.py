class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rs = [[s,i] for i,s in enumerate(rowSum)]
        cs = [[s,i] for i,s in enumerate(colSum)]
        rs.sort()
        cs.sort()
        N=len(rowSum)
        M=len(colSum)
        ans = [[0 for _ in range(M)] for _ in range(N)]
        i=j=0
        while i<N:
            rsval, rsi = rs[i]
            csval, csi = cs[j]
            ans[rsi][csi] = min(rsval,csval)
            if rsval==csval:
                i+=1
                j+=1
            elif rsval>csval:
                rs[i][0] -= csval
                j+=1
            else:
                cs[j][0] -= rsval
                i+=1
        return ans
                