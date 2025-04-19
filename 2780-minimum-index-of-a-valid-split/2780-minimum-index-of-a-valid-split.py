class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        major = nums[0]
        ct = 0
        for num in nums:
            if major==num:
                ct+=1
            else:
                ct-=1
                if ct==0:
                    major=num
        cts = [0]*N
        ct=0
        for i, num in enumerate(nums):
            if num==major:
                ct+=1
            else:
                ct-=1
            cts[i]=ct
        lastct = cts[-1]
        for i,num in enumerate(cts):
            if 0<num and num<lastct:
                return i
        return -1