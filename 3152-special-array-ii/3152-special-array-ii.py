class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        N=len(nums)
        compl = [(nums[i]^nums[i+1])&1 for i in range(N-1)]
        s = 0
        subsum = [0]
        for i in compl:
            s+=i
            subsum.append(s)
        ans = []
        for a,b in queries:
            if b-a == subsum[b]-subsum[a]:
                ans.append(True)
            else:
                ans.append(False)
        return ans