class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        conns = {wd:[] for wd in words}
        wds = set()
        def deterHamming1(wd1,wd2):
            if len(wd1)!=len(wd2):
                return False
            f=0
            for ch1, ch2 in zip(wd1,wd2):
                if ch1!=ch2:
                    f+=1
            return f==1
        for i, (j,wd) in enumerate(zip(groups,words)):
            for ii in range(i):
                if groups[ii] == j:
                    continue
                wd2 = words[ii]
                if deterHamming1(wd,wd2):
                    conns[wd2].append(wd)
        v = {wd:[0,""] for wd in words}
        maxlen = 0
        bestends = ""
        for wd in words:
            l,fr = v[wd]
            l+=1
            if l>maxlen:
                maxlen=l
                bestends=wd
            for nwd in conns[wd]:
                if v[nwd][0] < l:
                    v[nwd][0]=l
                    v[nwd][1]=wd
        ans = []
        while bestends:
            ans.append(bestends)
            bestends=v[bestends][1]

        return ans[::-1]