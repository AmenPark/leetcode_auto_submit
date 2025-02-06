class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        v = {p:0 for p in bank}
        v[startGene]=1
        q = [startGene]
        ans=0
        if startGene==endGene:
            return 0
        def genN(wd):
            for gene in bank:
                diff=0
                for ch1,ch2 in zip(gene,wd):
                    if ch1!=ch2:
                        diff+=1
                if diff==1:
                    yield gene

        while q:
            nq = []
            ans+=1
            for nd in q:
                for nnd in genN(nd):
                    if v[nnd]:
                        continue
                    v[nnd]=ans
                    nq.append(nnd)
            q=nq
            if v.get(endGene,0):
                return v[endGene]
        return -1
