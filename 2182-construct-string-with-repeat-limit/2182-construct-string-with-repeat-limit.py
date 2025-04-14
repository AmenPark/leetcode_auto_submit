class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = list(s)
        ans.sort(reverse=True)
        N=len(ans)
        i=0
        j=1
        ct=0
        nch = ""
        while i<N:
            if ans[i]!=nch:
                nch=ans[i]
                i+=1
                ct=1
                continue
            if ct<repeatLimit:
                i+=1
                ct+=1
                continue
            j=max(j,i+1)
            while j<N:
                if ans[j]==nch:
                    j+=1
                    continue
                break
            if j==N:
                return "".join(ans[:i])
            ans[i],ans[j] = ans[j],ans[i]
            nch=ans[i]
            ct=1
            i+=1
            j+=1
        return "".join(ans)