class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N=len(nums)
        l=collections.deque()
        ss=0
        ans=0
        for i in range(k):
            ns=0
            if ss^nums[i]==0:
                ns=1
                ans+=1
            l.append(ns)
            ss^=ns
        for i in range(k,N-k+1):
            ss^=l.popleft()
            ns=0
            if ss^nums[i]==0:
                ns=1
                ans+=1
            l.append(ns)
            ss^=ns
        for i in range(N-k+1,N):
            ss^=l.popleft()
            if nums[i]^ss==0:
                return -1
        return ans