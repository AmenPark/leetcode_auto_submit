class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diffs=[0]*(len(nums)+1)
        bval=0
        for i,n in enumerate(nums):
            diffs[i]=n-bval
            bval=n
        for a,b in queries:
            diffs[a] -= 1
            diffs[b+1] += 1
        ns = 0
        for d in diffs[:-1]:
            ns += d
            if ns>0:
                return False
        return True