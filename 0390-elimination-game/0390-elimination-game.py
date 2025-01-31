class Solution:
    def lastRemaining(self, n: int) -> int:
        idx=0
        filt=1
        tries=0
        while n>1:
            tries+=1
            if tries&1:
                idx += filt
            else:
                if n&1:
                    idx+=filt
            filt<<=1
            n//=2
        return idx+1