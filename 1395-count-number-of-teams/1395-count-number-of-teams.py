class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N=len(rating)+1
        val = [(n,i) for i,n in enumerate(rating)]
        val.sort()
        rating = [l[1] for l in val]
        incfw = [0]*N
        decfw=[0]*N
        onefw=[0]*N
        ans=0
        def getsum(fw, n):
            w=n
            rt=0
            while w:
                rt+=fw[w]
                w-=w&(-w)
            return rt
        def updatesum(fw,n,diff):
            w=n
            while w<N:
                fw[w]+=diff
                w+=w&(-w)
        
        for r in rating:
            ans += getsum(decfw, N-1) - getsum(decfw, r)
            ans += getsum(incfw, r-1)
            updatesum(incfw, r, getsum(onefw, r-1))
            updatesum(decfw, r, getsum(onefw,N-1)-getsum(onefw,r))
            updatesum(onefw, r, 1)
        return ans