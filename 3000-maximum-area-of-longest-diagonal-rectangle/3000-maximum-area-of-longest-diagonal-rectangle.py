class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag=0
        ans=0
        for a,b in dimensions:
            dg=a**2+b**2
            if dg>diag:
                diag=dg
                ans=a*b
            elif dg==diag:
                ans=max(ans,a*b)
        return ans