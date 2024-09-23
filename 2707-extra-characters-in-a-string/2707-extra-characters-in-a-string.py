class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = {}
        for wd in dictionary:
            d=trie
            for ch in wd:
                if ch not in d:
                    d[ch] = {}
                d=d[ch]
            d["."] = len(wd)
        l = [i for i in range(1, len(s)+1)]
        l.append(0)
        nds = [trie]
        for i,ch in enumerate(s):
            nnds = [trie]
            nval = min(i+1, l[i-1]+1)
            for d in nds:
                if ch in d:
                    nd = d[ch]
                    if "." in nd:
                        nval = min(nval, l[i-nd["."]])
                    nnds.append(nd)
            l[i]=nval
            nds=nnds
        return l[-2]