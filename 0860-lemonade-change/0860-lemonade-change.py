class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dct={5:0, 10:0, 20:0}
        for b in bills:
            if b==5:
                dct[5]+=1
            elif b==10:
                dct[10]+=1
                dct[5]-=1
                if dct[5]==-1:
                    return False
            else:
                dct[20] += 1
                if dct[10]>0:
                    dct[10]-=1
                    dct[5]-=1
                else:
                    dct[5]-=3
                if dct[5]==-1:
                    return False
        return True