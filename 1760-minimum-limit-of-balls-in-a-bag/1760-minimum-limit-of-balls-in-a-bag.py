class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l=sum(nums)//(len(nums)+maxOperations)
        if l==0:
            return 1
        def search(k):
            oper = 0
            for n in nums:
                oper += ((n-1)//k)
            return oper
        r=l
        while search(r)>maxOperations:
            r*=2
        while l<r-1:
            m=(l+r)//2
            if (w:=search(m))>maxOperations:
                l=m
            else:
                r=m
        return r
