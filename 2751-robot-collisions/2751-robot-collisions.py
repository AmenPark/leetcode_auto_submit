class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        l=[]
        for p,h,d in zip(positions, healths, directions):
            l.append((p,h,d))
        l.sort()
        result = {}
        rst = []
        for p,h,d in l:
            if d=="R":
                rst.append([h,p])
            else:
                while rst:
                    lh, lp = rst[-1]
                    if lh==h:
                        rst.pop()
                        h=0
                        break
                    elif lh<h:
                        rst.pop()
                        h-=1
                        continue
                    else:
                        rst[-1][0]=lh-1
                        h=0
                        break
                if h>0:
                    result[p]=h
        for lh,lp in rst:
            result[lp]=lh
        ans=[]
        for p in positions:
            if p in result:
                ans.append(result[p])
        return ans
