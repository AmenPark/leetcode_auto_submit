class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        M = ceil(sqrt((c)//2))
        MM = int(sqrt(c))+1
        for i in range(M,MM+1):
            tg=c-i*i
            if tg<0:
                break
            tg=sqrt(tg)
            if int(tg)==tg:
                return True
        return False