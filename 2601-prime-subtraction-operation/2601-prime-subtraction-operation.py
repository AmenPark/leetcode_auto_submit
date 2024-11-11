class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = [2]
        for i in range(3,1001,2):
            flag=True
            for p in primes:
                if i%p==0:
                    flag=False
                    break
            if flag:
                primes.append(i)
        lv = nums[-1]
        i=len(nums)-1
        while i:
            i-=1
            if lv>nums[i]:
                lv=nums[i]
                continue
            tg = nums[i] - lv + 1
            idx = bisect_left(primes,tg)
            nums[i] -= primes[idx]
            if nums[i]<=0:
                return False
            lv=nums[i]
        return True
