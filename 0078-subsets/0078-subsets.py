class Solution:
    def getsub(self, nums, i, now):
        if i==len(nums):
            self.ans.append(now[:])
            return
        self.getsub(nums,i+1,now)
        now.append(nums[i])
        self.getsub(nums,i+1,now)
        now.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.getsub(nums,0,[])
        return self.ans