class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bitor = lambda a,b:a|b
        tobit = lambda l:reduce(bitor, [1<<(ord(ch)-ord("a")) for ch in l], 0)
        allow = tobit(allowed)
        return sum([allow == (allow | tobit(string)) for string in words])
        