class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ct={}
        rev={}
        ans=[0]*len(nums)
        for i,n in enumerate(nums):
            ct[n]=ct.get(n,0)+1
            if n not in rev:
                rev[n]=[]
            rev[n].append(i)
        sks = sorted(list(ct.keys()))
        sidx=0
        bval=sks[0]
        for idx,key in enumerate(sks):
            if bval+limit>=key:
                bval=key
                continue
            hq=[]
            for i in range(sidx,idx):
                for ii in rev[sks[i]]:
                    heapq.heappush(hq,ii)
            for i in range(sidx,idx):
                val=sks[i]
                for _ in range(len(rev[val])):
                    ans[heapq.heappop(hq)]=val
            sidx=idx
            bval=key
        hq=[]
        for i in range(sidx,idx+1):
            for ii in rev[sks[i]]:
                heapq.heappush(hq,ii)
        for i in range(sidx,idx+1):
            val=sks[i]
            for _ in range(len(rev[val])):
                ans[heapq.heappop(hq)]=val
        return ans
    
