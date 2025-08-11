class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD=10**9+7
        i=1
        k=0
        powers=[]
        while i<=n:
            if i&n:
                powers.append(k)
            i<<=1
            k+=1
        ss = [0]
        s=0
        for p in powers:
            s+=p
            ss.append(s)
        ans = [(1<<(ss[b+1] - ss[a]))%MOD for a,b in queries]
        return ans
        