class Solution:
    def numSteps(self, s: str) -> int:
        ans=0
        i = len(s)-1
        while s[i] =="0":
            ans+=1
            i-=1
        if i==0:
            return ans
        while i>=0:
            if s[i] == "1":
                ans += 1
                i-=1
                continue
            while s[i]=="0":
                ans+=2
                i-=1
        return ans+1
