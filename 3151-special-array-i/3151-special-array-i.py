class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        p=1-(nums[0]&1)
        for n in nums:
            if (n&1)==p:
                return False
            p=1-p
        return True