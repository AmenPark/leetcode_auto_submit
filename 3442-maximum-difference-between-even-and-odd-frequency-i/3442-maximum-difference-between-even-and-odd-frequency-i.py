class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for ch in s:
            d[ch]=d.get(ch,0)+1
        maxOdd=1
        minEven=len(s)
        for v in d.values():
            if v&1:
                maxOdd=max(maxOdd,v)
            else:
                minEven=min(minEven,v)
        return maxOdd-minEven