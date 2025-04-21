class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        ss = 0
        minval = 0
        maxval = 0
        for n in differences:
            ss+=n
            minval = min(minval, ss)
            maxval = max(maxval, ss)
        return len(range(lower-minval, upper-maxval+1, 1))


