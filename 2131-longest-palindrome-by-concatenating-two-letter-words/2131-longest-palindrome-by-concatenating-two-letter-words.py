class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = {}
        ans = 0
        onlys = 0
        for wd in words:
            dw = wd[::-1]
            if dw==wd:
                if d.get(wd,0):
                    ans += 4
                    d[wd]-=1
                    onlys -= 1
                else:
                    d[wd]=d.get(wd,0)+1
                    onlys += 1
            elif d.get(dw,0):
                d[dw] -=1
                ans+=4
            else:
                d[wd]=d.get(wd,0)+1
        if onlys:
            ans+=2
        return ans