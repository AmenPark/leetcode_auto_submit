class Solution:
    def checkRecord(self, n: int) -> int:
        N = 10**9+7
        a = [1,0,0]
        b = [0,0,0]
        for i in range(n):
            ba = a[0]
            bb = b[0]
            a[0] = sum(a)%N
            b[0] = (sum(b) + a[0])%N
            b[2] = b[1]
            a[2] = a[1]
            a[1] = ba
            b[1] = bb
        return (sum(a) + sum(b))%N

