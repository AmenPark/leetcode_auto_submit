class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N=len(nums)
        idx=[0,0,0]
        r = 0
        while r<N:
            v=nums[r]
            for x in range(2,v-1,-1):
                nums[idx[x]]=x
                idx[x]+=1
            r+=1
            print(nums)
        