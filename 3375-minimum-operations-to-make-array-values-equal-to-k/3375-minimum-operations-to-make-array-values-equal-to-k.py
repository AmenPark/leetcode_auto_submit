class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        d=set()
        for n in nums:
            d.add(n)
        ans=0
        d.discard(k)
        for key in d:
            if key<k:
                return -1
            ans+=1
        return ans