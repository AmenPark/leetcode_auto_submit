class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bl = 0
        for ch in brokenLetters:
            bl |= 1<<(ord(ch)-ord('a'))
        wds=text.split()
        ans = len(wds)
        for wd in wds:
            for ch in wd:
                if (1<<(ord(ch)-ord('a'))&bl):
                    ans-=1
                    break
        return ans