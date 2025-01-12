class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        ss = []
        s = 0
        for n in nums:
            s+=n
            ss.append(s)
        print(bisect_right([1,2,2,3,3,3], 3))
        print(bisect_left([1,2,2,3,3,3],3))
        def p(mid):
            s=0
            l=1
            for n in nums:
                if n>mid:
                    return False
                if n+s<=mid:
                    s+=n
                else:
                    s=n
                    l+=1
            if l>k:
                return False
            return True
                
        l=1
        r=10**9
        while l<r-1:
            mid=(l+r)//2
            if p(mid):
                r=mid
            else:
                l=mid
            
        return r
