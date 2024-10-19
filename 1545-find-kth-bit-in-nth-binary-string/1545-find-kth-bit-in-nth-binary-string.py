class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        transpos = 0
        nk = k-1
        for i in range(n-1,0,-1):
            nl = 2**i - 1
            if nk > nl:
                transpos ^= 1
                nk = nl - (nk - nl)
            elif nk == nl:
                return 1^transpos
        return str(transpos)
            