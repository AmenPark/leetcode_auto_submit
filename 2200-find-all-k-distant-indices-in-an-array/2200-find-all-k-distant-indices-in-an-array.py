class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        kidxs = [i for i,n in enumerate(nums) if n==key]
        bi = 0
        ans=[]
        N=len(nums)
        for idx in kidxs:
            for j in range(max(bi, idx-k), min(idx+k+1,N)):
                ans.append(j)
            bi=idx+k+1
        return ans