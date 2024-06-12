class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N=len(nums)
        i=0
        j=0
        k=N
        r = 0
        while r<N:
            v=nums[r]
            if v==2:
                k-=1
            else:
                nums[j]=1
                j+=1
                if v==0:
                    nums[i]=0
                    i+=1
            r+=1
        for x in range(k,N):
            nums[x]=2
            