class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hq=[]
        for i,num in enumerate(nums):
            heapq.heappush(hq, (num,i))

        for _ in range(k):
            v,idx = heapq.heappop(hq)
            v*=multiplier
            nums[idx]=v
            heapq.heappush(hq,(v,idx))
        return nums
