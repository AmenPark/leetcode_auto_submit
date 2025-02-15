class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            nn = n
            sd = 0
            while nn:
                sd += nn%10
                nn//=10
            if sd not in d:
                d[sd] = []
            heapq.heappush(d[sd],n)
            if len(d[sd])>=3:
                heapq.heappop(d[sd])
        ans=-1
        for k,v in d.items():
            if len(v)==2:
                ans=max(ans,sum(v))
        return ans