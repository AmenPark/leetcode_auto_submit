class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        d=time//(n-1)
        r=time%(n-1)
        if d%2==0:
            return r+1
        else:
            return n-r