class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        mods = [[] for _ in range(k)]
        for n in nums:
            heapq.heappush(mods[n%k],n)
        chains = []
        for hq in mods:
            if not hq:
                continue
            chain = []
            bv = hq[0]-k
            while hq:
                v = heapq.heappop(hq)
                if v==bv:
                    chain[-1] += 1
                elif v==bv+k:
                    chain.append(1)
                else:
                    chains.append(chain)
                    chain = [1]
                bv = v
            chains.append(chain)
        vals = []
        print(chains)
        for chain in chains:
            bused=0
            bnot=1
            for v in chain:
                usecase = (1<<v) - 1
                used = usecase * bnot
                notused = bused + bnot
                bused = used
                bnot = notused
            vals.append(bused+bnot)
        ans = 1
        for v in vals:
            ans*=v
        return ans-1
