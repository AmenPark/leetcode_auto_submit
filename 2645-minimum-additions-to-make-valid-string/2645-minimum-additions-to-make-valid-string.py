class Solution:
    def addMinimum(self, word: str) -> int:
        wd2num={"a":0,"b":1,"c":2}
        bval=2
        ans=0
        for ch in word:
            val=wd2num[ch]
            ans += (val-bval-1)%3
            bval = val
        ans += (0-bval-1)%3
        return ans