class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        d = {}
        for n in nums:
            pn = n%k
            for i in range(k):
                d[(i,pn)] = max(d.get((i,pn),0), d.get((pn,i),0)+1)
        return max(d.values())