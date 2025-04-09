class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        d=set()
        for n in nums:
            if n in d:
                continue
            if n<k:
                return -1
            d.add(n)
        d.discard(k)
        return len(d)