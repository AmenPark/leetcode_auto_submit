class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        limits = str(n)
        w = 1
        while w<=n:
            w*=10
        val = (w-1)//9
        def count_prefix(prefix):
            count=0
            current=prefix
            nprefix = prefix+1
            while current<=n:
                count+=min(n+1,nprefix)-current
                current*=10
                nprefix*=10
            return count
        
        ans=0
        cur=0
        i=1
        k-=1
        while k:
            ct= count_prefix(i)
            print(ct)
            if ct<=k:
                k -= ct
                i+=1
                continue
            else:
                i*=10
                k -= 1
                continue
        

        return i

            
