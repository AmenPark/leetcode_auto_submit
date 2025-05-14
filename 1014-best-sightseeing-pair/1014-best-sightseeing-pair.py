class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        l = [v-i for i,v in enumerate(values)]
        N=len(values)
        bests = [(N-1, l[N-1])]
        bestval=l[-1]
        for i in range(N-2,-1,-1):
            if l[i]>bestval:
                bests.append((i,l[i]))
                bestval=l[i]
        ans=0
        for i,score in enumerate(l[:-1]):
            if bests[-1][0]==i:
                bests.pop()
            ans = max(ans, i*2 + score + bests[-1][1])
        return ans