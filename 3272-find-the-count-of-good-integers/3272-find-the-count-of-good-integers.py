class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        vals = []
        kk=n-1
        i=0
        sset=set()
        while i<kk:
            vals.append(1*(10**i)+1*(10**kk))
            i+=1
            kk-=1
        if i==kk:
            mid = 10**i
            mid%=k
        mods = [v%k for v in vals]
        self.ans=0
        fct=[1]
        def fact(i):
            if len(fct)>i:
                return fct[i]
            while len(fct)<=i:
                fct.append(fct[-1]*len(fct))
            return fct[i]
        def addsum(ct):
            # print(ct,self.ans,end=" ")
            if tuple(ct) in sset:
                # print(self.ans)
                return
            sset.add(tuple(ct))
            tval=1
            for v in ct:
                tval*=fact(v)
            tval=fact(n)//tval
            if ct[0]==0:
                self.ans+=tval
                # print(self.ans)
                return
            zval = 1
            ct[0]-=1
            for v in ct:
                zval*=fact(v)
            ct[0]+=1
            zval = fact(n-1)//zval
            self.ans += tval-zval
            # print(self.ans)
            
        def kpal(i,ms,ct):
            # print(i,ms,ct)
            if i==len(mods):
                if n%2==0:
                    if ms==0:
                        addsum(ct)
                    return
                else:
                    for ii in range(10):
                        mmod = (mid*ii)%k
                        if (mmod+ms)%k==0:
                            ct[ii]+=1
                            addsum(ct)
                            ct[ii]-=1
                    return
            s=0
            if i==0:
                s=1
            modval = mods[i]
            for cnum in range(s,10):
                mms = (ms+modval*cnum)%k
                ct[cnum]+=2
                kpal(i+1, mms, ct)
                ct[cnum]-=2
        kpal(0, 0, [0]*10)
        return self.ans