class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        N=len(t)
        i=0
        tg=t[i]
        for ch in s:
            if ch==tg:
                i+=1
                if i==N:
                    break
                tg=t[i]
        return N-i