class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def oper1(t1,t2):
            a,b=t1
            c,d=t2
            return (a*d+b*c,b*d)
        def oper2(t1,t2):
            a,b=t1
            c,d=t2
            return (a*d-b*c,b*d)
        def oper3(t1,t2):
            a,b=t1
            c,d=t2
            return (a*d,b*c)
        def oper4(t1,t2):
            a,b=t1
            c,d=t2
            return(a*c,b*d)
        def oper5(t1,t2):
            a,b=t1
            c,d=t2
            return(b*c-a*d,b*d)
        def oper6(t1,t2):
            a,b=t1
            c,d=t2
            return(b*c,a*d)
        opers=[oper1,oper2,oper3,oper4,oper5,oper6]
        a,b,c,d=cards
        ab=[oper((a,1),(b,1)) for oper in opers]
        ac=[oper((a,1),(c,1)) for oper in opers]
        ad=[oper((a,1),(d,1)) for oper in opers]
        bc=[oper((b,1),(c,1)) for oper in opers]
        bd=[oper((b,1),(d,1)) for oper in opers]
        cd=[oper((c,1),(d,1)) for oper in opers]
        def chec(g1, g2):
            for t1 in g1:
                for t2 in g2:
                    for oper in opers:
                        r1, r2 = oper(t1,t2)
                        if r2!=0 and r1%r2==0 and r1//r2 == 24:
                            print("**", t1, t2)
                            return True
            return False
        if chec(ab,cd):
            return True
        if chec(ac,bd):
            return True
        if chec(ad,bc):
            return True
        def conc(xy,q,to_add=[]):
            for t in xy:
                for oper in opers:
                    to_add.append((oper(t,(q,1))))
            return to_add
        abc = conc(bc,a,conc(ac,b,conc(ab,c,[])))
        if chec(abc,[(d,1)]):
            return True
        abd = conc(bd,a,conc(ad,b,conc(ab,d,[])))
        if chec(abd,[(c,1)]):
            return True
        acd = conc(cd,a,conc(ad,c,conc(ac,d,[])))
        if chec(acd,[(b,1)]):
            return True
        bcd = conc(cd,b,conc(bd,c,conc(bc,d,[])))
        if chec(bcd,[(a,1)]):
            return True
        
        return False
        