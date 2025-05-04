class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d={}
        ans=0
        for a,b in dominoes:
            tg = (1<<a) | (1<<b)
            ans+=d.get(tg,0)
            d[tg]=d.get(tg,0)+1
        return ans