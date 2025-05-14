class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        Z=len(nums[0])
        hq=[]
        for n in nums:
            heapq.heappush(hq, int(n,2))
        i=0
        while hq:
            if hq[0]>i:
                return bin(i)[2:].zfill(Z)
            heapq.heappop(hq)
            i+=1
        return bin(i)[2:].zfill(Z)