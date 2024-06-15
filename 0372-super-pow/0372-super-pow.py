class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        N=1337
        a%=N
        unit = a
        a=1
        while b:
            tg = b.pop()
            a *= unit**tg
            a%=N
            unit=unit**10
            unit%=N
        return a