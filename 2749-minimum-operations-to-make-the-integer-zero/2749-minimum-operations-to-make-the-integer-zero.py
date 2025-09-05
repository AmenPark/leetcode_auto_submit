class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        def ctbit(n):
            if n<0:
                return 0
            rt=0
            while n:
                if n&1:
                    rt+=1
                n=n>>1
            return rt
        tg = num1
        ans = 0
        while tg>0:
            tg -= num2
            ans += 1
            if ctbit(tg) <= ans and tg >= ans:
                return ans
        return -1