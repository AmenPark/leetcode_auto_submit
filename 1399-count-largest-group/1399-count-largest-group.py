class Solution:
    def countLargestGroup(self, n: int) -> int:
        ans = [0]*40
        for i in range(1,n+1):
            v = 0
            while i:
                v+=i%10
                i//=10
            ans[v]+=1
        mv = 0
        rt = 0
        for i,v in enumerate(ans):
            if v>mv:
                rt=1
                mv=v
            elif v==mv:
                rt+=1
        return rt