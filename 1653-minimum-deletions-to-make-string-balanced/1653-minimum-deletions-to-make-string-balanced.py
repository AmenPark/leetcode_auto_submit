class Solution:
    def minimumDeletions(self, s: str) -> int:
        act=0
        for ch in s:
            if ch=="a":
                act+=1
        bct=0
        ans = act
        for ch in s:
            if ch=="a":
                act -= 1
            else:
                bct += 1
            ans = min(ans, act+bct)
        return ans