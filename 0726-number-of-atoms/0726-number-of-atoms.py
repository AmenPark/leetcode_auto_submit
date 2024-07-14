class Solution:
    def countOfAtoms(self, formula: str) -> str:
        l=[]
        st=[]
        cur=l
        for ch in formula:
            if ch=="(":
                cur.append([])
                st.append(cur)
                cur=cur[-1]
            elif ch==")":
                cur=st.pop()
            else:
                cur.append(ch)
        ct={}
        def getct(l,times):
            tg=""
            nn=0
            for ch in l:
                if type(ch)==str: 
                    if ch.isdigit():
                        nn*=10
                        nn+=int(ch)
                        continue
                if type(ch)==str and ch.islower():
                    tg+=ch
                    continue
                else:
                    nn=max(nn,1)
                    if type(tg)==list:
                        getct(tg,nn*times)
                    elif tg:
                        ct[tg]=ct.get(tg,0)+times*nn
                    nn=0
                    tg=ch
            if type(tg)==list:
                getct(tg,times*max(nn,1))
            else:
                ct[tg]=ct.get(tg,0)+times*max(nn,1)
        getct(l,1)
        k=list(ct.keys())
        print(ct)
        k.sort()
        ans=[]
        for key in k:
            ans.append(key)
            if ct[key]>1:
                ans.append(str(ct[key]))
        return "".join(ans)