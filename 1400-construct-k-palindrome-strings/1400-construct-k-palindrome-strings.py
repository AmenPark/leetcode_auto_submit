class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        ct={}
        for ch in s:
            ct[ch]=ct.get(ch,0)+1
        odds = 0
        for ch, num in ct.items():
            if num%2:
                odds+=1
        if odds>k:
            return False
        return True