class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n&(n-1)==0 and (1431655765&n>0)