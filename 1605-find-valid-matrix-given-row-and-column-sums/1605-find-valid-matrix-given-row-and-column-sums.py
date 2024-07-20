class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N=len(rowSum)
        M=len(colSum)
        ans = [[0 for _ in range(M)] for _ in range(N)]
        i=j=0
        rss=iter(rowSum)
        css=iter(colSum)
        rs=next(rss)
        cs=next(css)
        while i<N:
            if rs==cs:
                ans[i][j] = colSum[j]
                i+=1
                j+=1
                rs=next(rss,-1)
                cs=next(css,-1)
            elif rs>cs:
                ans[i][j] = cs 
                rs -= cs
                j+=1
                cs=next(css,-1)
            else:
                ans[i][j]=rs
                cs -= rs
                i+=1
                rs=next(rss,-1)
        return ans
                