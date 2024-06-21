class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        m=0
        nM=0
        ans=0
        for i,(c,g) in enumerate(zip(customers,grumpy)):
            if g==0:
                ans+=c
            else:
                nM+=c
            j=i-minutes
            if j>=0:
                if grumpy[j]==1:
                    nM-=customers[j]
            m=max(m,nM)

        
        return ans+m