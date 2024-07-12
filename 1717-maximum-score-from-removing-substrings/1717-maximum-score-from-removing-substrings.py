class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        l=[[]]
        for ch in s:
            if ch in "ab":
                l[-1].append(ch)
            else:
                l.append([])
        a="a"
        b="b"
        if y>x:
            a,b=b,a
            x,y=y,x
        def trueG(l):
            if len(l)<=1:
                return 0
            if len(l)==2:
                return min(l) * x
            if len(l)==3:
                rt = min(l[0],l[1])*x
                if l[1]>l[0]:
                    rt += min(l[1]-l[0], l[2])*y
                return rt
            lastpop=0
            if len(l)%2 == 1:
                lastpop=l.pop()
            ctb=l.pop()
            cta=l.pop()
            rt=min(cta,ctb)*x
            if cta>ctb:
                lastpop += cta-ctb
            else:
                l[-1]+=ctb-cta
            if lastpop:
                l.append(lastpop)
            return rt+trueG(l)
        def falseG(l):
            if len(l)<=1:
                return 0
            if len(l)==2:
                return min(l)*y
            if len(l)==3:
                rt=min(l[1],l[2])*x
                if l[1]>l[2]:
                    rt += min(l[1]-l[2], l[0])*y
                return rt
            lastpop = 0
            if len(l)%2==0:
                lastpop=l.pop()
            ctb=l.pop()
            cta=l.pop()
            rt=min(cta,ctb)*x
            if cta>ctb:
                lastpop += cta-ctb
            else:
                l[-1]+=ctb-cta
            if lastpop:
                l.append(lastpop)
            return rt+falseG(l)

        def maxG(l):
            if len(l)<=1:
                return 0
            bch = l[0]
            ct=[0]
            for ch in l:
                if ch==bch:
                    ct[-1]+=1
                else:
                    bch=ch
                    ct.append(1)
            fch = l[0]
            if fch==a:
                return trueG(ct)
            return falseG(ct)
        ans =0
        for arr in l:
            ans += maxG(arr)
        return ans