class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ct={}
        for ch in ransomNote:
            ct[ch]=ct.get(ch,0)+1
        for ch in magazine:
            ct[ch]=ct.get(ch,1)-1
        for v in ct.values():
            if v:
                return False
        return True