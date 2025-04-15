class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ct = [0,0,0]
        flag=0
        N=len(s)
        ans=0
        j=0
        for i,ch in enumerate(s):
            tg = ord(ch)-ord('a')
            ct[tg]+=1
            if ct[tg]==1:
                flag+=1
            while flag==3:
                ans += N-i
                dch = s[j]
                dtg = ord(dch)-ord('a')
                ct[dtg] -= 1
                if ct[dtg]==0:
                    flag-=1
                j+=1
        return ans
            