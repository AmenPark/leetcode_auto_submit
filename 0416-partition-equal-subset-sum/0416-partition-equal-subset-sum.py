class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ss = sum(nums)
        if ss&1:
            return False
        tg=ss//2
        s={0}
        for n in nums:
            ns={i for i in s}
            for i in s:
                ns.add(i+n)
            s=ns
            if tg in s:
                return True
        return False