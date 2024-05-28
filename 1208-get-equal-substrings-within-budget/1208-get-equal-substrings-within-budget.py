class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        q=[0]
        ss=0
        for x,y in zip(s,t):
            ss+=abs(ord(x)-ord(y))
            q.append(ss)
        N = len(q)
        l=0
        ans = 0
        r=1
        while r<N:
            if q[r] - q[l] <=maxCost:
                ans=max(ans,r-l)
                r+=1
            else:
                l+=1
        return ans