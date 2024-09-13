class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xl = [0]
        s=0
        for v in arr:
            s^=v
            xl.append(s)
        ans = []
        for x,y in queries:
            ans.append(xl[y+1]^xl[x])
        return ans