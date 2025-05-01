class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N=len(weights)
        k=min(k, N+1-k)
        l = [weights[i]+weights[i-1] for i in range(1,N)]
        l.sort()
        return sum(l[-k:]) - sum(l[:k])

        