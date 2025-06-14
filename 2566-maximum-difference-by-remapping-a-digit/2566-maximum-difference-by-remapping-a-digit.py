class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        minval = int(s.replace(s[0],"0"))
        for ch in s:
            if ch!="9":
                break
        maxval = int(s.replace(ch, "9"))

        return maxval-minval