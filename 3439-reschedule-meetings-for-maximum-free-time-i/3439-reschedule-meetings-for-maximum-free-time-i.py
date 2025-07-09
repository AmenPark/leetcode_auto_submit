class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        s=0
        for i in range(k):
            s+=endTime[i]-startTime[i]
        beforeEnd=0
        ans=0
        for i in range(k,len(startTime)):
            ans = max(ans,startTime[i]-beforeEnd-s)
            beforeEnd=endTime[i-k]
            s-=endTime[i-k]-startTime[i-k]
            s+=endTime[i]-startTime[i]
        ans=max(ans, eventTime - beforeEnd - s)
        return ans