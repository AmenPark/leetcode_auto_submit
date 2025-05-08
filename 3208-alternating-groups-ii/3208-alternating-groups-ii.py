class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N=len(colors)
        diffs = [0]*N
        for i in range(N):
            if colors[i]!=colors[i-1]:
                diffs[i]=1
        sc = 0
        i=0
        while i<N:
            if diffs[i]==1:
                sc+=1
                i+=1
            else:
                break
        if i==N:
            return N
        d={}
        nc = 1
        while i<N:
            if diffs[i]==0:
                d[nc]=d.get(nc,0)+1
                nc=1
            else:
                nc+=1
            i+=1
        d[sc+nc]=d.get(sc+nc,0)+1
        print(d)
        ans=0
        for length,v in d.items():
            if length>=k:
                ans += v*(length-k+1)
        return ans