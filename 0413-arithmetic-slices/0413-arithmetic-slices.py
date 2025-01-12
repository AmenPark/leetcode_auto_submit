class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        diffs = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
        
        ans = 0
        ct = 0
        bval = diffs[0]
        for diff in diffs:
            if bval==diff:
                ct+=1
            else:
                ans += ((ct-1) * (ct))//2
                ct=1
                bval=diff
        ans+=((ct-1)*(ct))//2
        return ans