class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        N=len(pref)
        ans=0
        for wd in words:
            if wd[:N]==pref:
                ans+=1
        return ans