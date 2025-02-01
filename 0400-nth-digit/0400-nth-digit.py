class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1~9 -> 9가지
        # 10~99 -> 90가지
        #100~999 -> 900가지
        if n<10:
            return n
        f = 9
        idx=1
        while n>f*idx:
            n-=f*idx
            f*=10
            idx+=1
        pos=n%idx
        number = n//idx + 10**(idx-1)
        if pos==0:
            number-=1
            
        val = str(number)[pos-1]
        return int(val)