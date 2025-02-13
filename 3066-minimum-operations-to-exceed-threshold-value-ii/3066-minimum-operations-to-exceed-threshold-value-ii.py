class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans=0
        while nums[0]<k:
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)
            heapq.heappush(nums, a*2+b)
            ans+=1
        return ans