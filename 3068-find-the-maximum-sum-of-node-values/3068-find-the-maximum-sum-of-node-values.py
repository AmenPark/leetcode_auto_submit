class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        S = sum(nums)
        diffs = [(x^k)-x for x in nums]
        diffs.sort()
        while len(diffs)>1:
            if diffs[-2] >= 0:
                S+=diffs.pop()
                S+=diffs.pop()
            else:
                break
        ans = S
        if len(diffs)>1:
            ans = max(ans, ans+diffs[-1]+diffs[-2])
        return ans