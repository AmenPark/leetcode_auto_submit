class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        ct={}
        for ch in s:
            ct[ch]=ct.get(ch,0)+1
        for ch, num in ct.items():
            if num&1:
                k-=1
        if k>0:
            return False
        return True