class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rdxs = {}
        ldxs = {}
        for i,ch in enumerate(s):
           rdxs[ch] = i
           ldxs[ch] = ldxs.get(ch,i)
        ca=[]
        for k,v in rdxs.items():
            v2 =ldxs[k]
            ca.append((v2,0))
            ca.append((v,1))
        ca.sort()
        ans=[]
        d=0
        bj = -1
        for v,io in ca:
            if io==0:
                d+=1
            else:
                d-=1
            if d==0:
                ans.append(v-bj)
                bj=v
        return ans