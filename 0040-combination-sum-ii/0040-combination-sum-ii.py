class Solution:
    def getCase(self, candidates, target, i, making):
        if target == 0:
            self.ans.append(making[:])
            return
        if i==-1:
            return
        else:
            v = candidates[i]
            self.getCase(candidates, target, i-1, making)
            for repeat in range(self.cdic[v]):
                if v<=target:
                    making.append(v)
                    target -= v
                    self.getCase(candidates, target, i-1, making)
                else:
                    break
            while making and making[-1]==v:
                making.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.cdic = {}
        for i in candidates:
            self.cdic[i]=self.cdic.get(i,0)+1
        keys = list(self.cdic.keys())
        keys.sort()
        N=len(keys)
        self.ans = []
        self.getCase(keys, target, N-1, [])
        return self.ans