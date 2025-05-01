class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        M=0
        m=0
        ss=0
        for n in nums:
            ss+=n
            M=max(M,ss)
            m=min(m,ss)
        return M-m