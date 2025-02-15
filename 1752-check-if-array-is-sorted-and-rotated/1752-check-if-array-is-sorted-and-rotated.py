class Solution:
    def check(self, nums: List[int]) -> bool:
        f=False
        bn = nums[0]
        for n in nums:
            if bn>n:
                if f:
                    return False
                f=True
            bn=n
        if f==True and nums[-1]>nums[0]:
            return False
        return True