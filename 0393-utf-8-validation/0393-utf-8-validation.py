class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        ps = [0, 1<<7, 3<<6, 7<<5, 15<<4, 31<<3]
        filter1=3<<6
        filter2=1<<7
        nc = 0
        for d in data:
            if nc>0:
                if filter1&d == filter2:
                    nc-=1
                    continue
                return False
            f=filter2
            while f&d:
                nc+=1
                f>>=1
            if nc>4:
                return False
            if nc==1:
                return False
            if nc>0:
                nc-=1
        if nc>0:
            return False
        return True