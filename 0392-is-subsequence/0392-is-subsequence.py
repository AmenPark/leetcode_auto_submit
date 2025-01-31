class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx=0
        N=len(s)
        for ch in t:
            if ch==s[idx]:
                idx+=1
                if idx==N:
                    return True
        return False