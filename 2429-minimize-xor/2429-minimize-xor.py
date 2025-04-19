class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def countbits(num):
            ans = 0
            while num:
                w=num&(-num)
                num-=w
                ans+=1
            return ans
        bt1 = countbits(num1)
        bt2 = countbits(num2)
        if bt1==bt2:
            return num1
        if bt1>bt2:
            leftbits = bt1-bt2
            leftval = 0
            tg = bt1
            for _ in range(leftbits):
                w=tg & (-tg)
                leftval += w
                tg -= w
            return num1 - leftval
        ans=0
        i=1
        for _ in range(bt2-bt1):
            while i&num1:
                i<<=1
            ans+=i
            i<<=1
        return ans+num1