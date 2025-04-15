class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N=len(nums)
        i=0
        while i<N-1:
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
                i+=2
            else:
                i+=1
        i=0
        j=0
        while i<N:
            if nums[i]:
                i+=1
                continue
            j=max(j,i+1)
            while j<N:
                if nums[j]==0:
                    j+=1
                else:
                    break
            if j==N:
                break
            nums[i]=nums[j]
            nums[j]=0
            i+=1
            j+=1
        return nums