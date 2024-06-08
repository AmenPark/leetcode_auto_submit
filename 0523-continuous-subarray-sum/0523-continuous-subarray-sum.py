class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = set()
        ssum = 0
        bsum = 0
        for n in nums:
            ssum += n
            ssum %= k
            if ssum in s:
                return True
            s.add(bsum)
            bsum=ssum
        return False