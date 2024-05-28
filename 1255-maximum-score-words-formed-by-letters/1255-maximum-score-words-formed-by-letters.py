class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # 8 bit for every characters, 1 bit for validations
        filter = 0
        k=1<<8
        for i in range(26):
             filter += k
             k<<=9

        def wd2num(wd):
            pool = 0
            ssum = 0
            for ch in wd:
                tg = ord(ch) - 97
                ssum += score[tg]
                pool += 1<<((tg)*9)
            return pool, ssum
        pool = wd2num(letters)[0]
        wdpools = [wd2num(wd) for wd in words]
        N = len(wdpools)
        ans = 0
        def getcase(pool, i):
            if i==N:
                return 0
            ans = getcase(pool,i+1)
            p,s = wdpools[i]
            pool -= p
            if (pool & filter)==0:
                ans = max(ans, getcase(pool,i+1)+s)
            return ans
        return getcase(pool,0)