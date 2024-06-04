class Solution:
    def scoreOfString(self, s: str) -> int:
        n=0
        for x,y in zip(s,s[1:]):
            n+=abs(ord(x)-ord(y))
        return n