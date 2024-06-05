class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cts = {}
        for ch in words[0]:
            cts[ch] = cts.get(ch,0)+1
        for wd in words[1:]:
            cts2={}
            for ch in wd:
                if cts.get(ch,0):
                    cts2[ch]=cts2.get(ch,0)+1
                    cts[ch]-=1
            cts=cts2

        l = []
        for k,v in cts.items():
            for _ in range(v):
                l.append(k)
        return l