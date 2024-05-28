class Solution:
    def getpart(self,s,i,now):
        if i==len(s):
            self.ans.append(now[:])
        for j in range(i+1,len(s)+1):
            wd = s[i:j]
            if wd == wd[::-1]:
                now.append(wd)
                self.getpart(s,j,now)
                now.pop()
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.getpart(s,0,[])
        return self.ans