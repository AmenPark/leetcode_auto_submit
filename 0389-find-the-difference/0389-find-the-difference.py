class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for ch in t:
            d[ch]=d.get(ch,0)+1
        for ch in s:
            d[ch]-=1
        for ch, val in d.items():
            if val:
                return ch