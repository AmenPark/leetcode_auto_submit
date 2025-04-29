class Solution:
    def canChange(self, start: str, target: str) -> bool:
        lct = 0
        rct = 0
        for sch, tch in zip(start,target):
            if sch=="R":
                rct+=1
            if tch=="L":
                lct+=1
            if lct>0 and rct>0:
                return False
            if sch=="L":
                lct -=1
            if tch=="R":
                rct-=1
            if lct<0 or rct<0:
                return False
        if lct==0 and rct==0:
            return True
        return False        