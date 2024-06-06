class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        cts = {}
        for h in hand:
            cts[h]=cts.get(h,0)+1
        keys=sorted(list(cts.keys()))
        for k in keys:
            if cts[k]==0:
                continue
            t = cts[k]
            for i in range(k,k+groupSize):
                cts[i] = cts.get(i,0)-t
                if cts[i]<0:
                    return False
        return True
