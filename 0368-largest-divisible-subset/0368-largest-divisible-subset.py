class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        to_do = iter(nums)
        ess={1:(0,0)}
        maxval = 0
        maxcase = 0
        if nums[0] == 1:
            next(to_do)
            ess[1]=(1,0)
            maxcase = 1
        for n in to_do:
            bc = 0
            bi = 0
            for k,(v1,v2) in ess.items():
                if n%k==0:
                    if bc<v1:
                        bc=v1
                        bi=k
            bc+=1
            ess[n] = (bc,bi)
            if maxval < bc:
                maxval = bc
                maxcase = n
        ans = []
        while maxcase != 0:
            ans.append(maxcase)
            maxcase = ess[maxcase][1]
        return ans