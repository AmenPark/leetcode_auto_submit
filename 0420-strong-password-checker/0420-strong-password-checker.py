class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        tpnum = {}
        lowerflag = False
        upperflag=False
        digitflag=False
        l=len(password)
        ct=0
        bch=""
        for ch in password:
            if 48<=ord(ch)<=57:
                digitflag=True
            elif 65<=ord(ch)<=90:
                upperflag=True
            elif 97<=ord(ch)<=122:
                lowerflag=True
            if ch==bch:
                ct+=1
            else:
                if ct>=3:
                    tpnum[ct]=tpnum.get(ct,0)+1
                bch=ch
                ct=1
        if ct>=3:
            tpnum[ct]=tpnum.get(ct,0)+1
        falseflag = 3-(int(lowerflag)+int(upperflag)+int(digitflag))
        if l<6:
            return max(6-l, falseflag)
        if l<=20:
            cnum = 0
            for k,v in tpnum.items():
                cnum += v*(k//3)
            return max(falseflag, cnum)
        mods = [[],[],[]]
        for k,v in tpnum.items():
            for _ in range(v):
                mods[k%3].append(k)
        to_del = l-20
        while to_del:
            if mods[0]:
                k=mods[0].pop()
                k-=1
                if k>2:
                    mods[2].append(k)
            elif mods[1]:
                k=mods[1].pop()
                k-=1
                mods[0].append(k)
            elif mods[2]:
                k=mods[2].pop()
                k-=1
                mods[1].append(k)
            else:
                break
            to_del -= 1
        ex = 0
        for c in mods:
            for v in c:
                ex += v//3
        return (l-20) + max(ex, falseflag)