class Solution:
    def firstUniqChar(self, s: str) -> int:
        cts={}
        firsts=set()
        for i, ch in enumerate(s):
            if ch in cts:
                firsts.add(ch)
            else:
                cts[ch]=i
        for ch in firsts:
            del cts[ch]
        if not cts:
            return -1
        return min(cts.values())