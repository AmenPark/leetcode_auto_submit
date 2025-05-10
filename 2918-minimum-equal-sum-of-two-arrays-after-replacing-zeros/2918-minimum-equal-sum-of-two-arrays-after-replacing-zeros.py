class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zl = 0
        zr = 0
        sl = 0
        sr = 0
        for n in nums1:
            if n:
                sl+=n
            else:
                zl+=1
        for n in nums2:
            if n:
                sr+=n
            else:
                zr+=1
        if zl==0:
            if zr==0:
                if sl==sr:
                    return sl
                return -1
            if sl < sr+zr:
                return -1
            return sl
        if zr==0:
            if sl+zl > sr:
                return -1
            return sr
        return max(sl+zl, sr+zr)