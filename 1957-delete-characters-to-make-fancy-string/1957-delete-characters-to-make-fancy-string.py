class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=[]
        bch=""
        ct=0
        for ch in s:
            if ch==bch:
                ct+=1
                if ct>2:
                    continue
            else:
                bch=ch
                ct=1
            ans.append(ch)
        return "".join(ans) 