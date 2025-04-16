class Solution:
    def maximumLength(self, s: str) -> int:
        bch = s[0]
        counts = [{} for _ in range(26)]
        rowct = 0
        for ch in s:
            if ch!=bch:
                chnum = ord(bch)-ord('a')
                counts[chnum][rowct] = counts[chnum].get(rowct,0)+1
                rowct=1
                bch=ch
            else:
                rowct +=1
        counts[ord(s[-1])-ord('a')][rowct] = counts[ord(s[-1])-ord('a')].get(rowct,0)+1
        ans = 0
        for d in counts:
            val = 0
            if d:
                mk = max(d.keys())
                if d[mk]>=3:
                    ans=max(ans,mk)
                elif d[mk]*2 + d.get(mk-1,0)>=3:
                    ans=max(ans,mk-1)
                else:
                    ans=max(ans,mk-2) 
        return ans or -1
            