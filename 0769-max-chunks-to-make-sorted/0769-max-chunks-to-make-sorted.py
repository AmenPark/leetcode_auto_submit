class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        ss=0
        tg=0
        for i,n in enumerate(arr):
            ss+=n
            tg+=i
            if tg==ss:
                ans+=1
        return ans