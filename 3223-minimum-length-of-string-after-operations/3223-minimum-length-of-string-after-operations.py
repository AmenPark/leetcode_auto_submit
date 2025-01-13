class Solution:
    def minimumLength(self, s: str) -> int:
        cts = {}
        for ch in s:
            cts[ch]=cts.get(ch,0)+1
        ans=0
        for k,v in cts.items():
            ans += (v%2) or 2
        return ans