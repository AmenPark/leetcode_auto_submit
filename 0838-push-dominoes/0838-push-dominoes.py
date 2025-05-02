class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N=len(dominoes)
        l = [N+1 for _ in range(N)]
        bi = "L"
        val=0
        for i,ch in enumerate(dominoes):
            if ch=="L":
                bi="L"
                val=0
            elif ch=="R":
                bi="R"
                l[i]=0
                val=0
            else:
                if bi=="R":
                    val+=1
                    l[i]=val
        bi="R"
        val=0
        for i in range(N-1,-1,-1):
            ch=dominoes[i]
            if ch=="R":
                bi="R"
                val=0
                l[i]="R"
            elif ch=="L":
                bi="L"
                val=0
                l[i]="L"
            else:
                if bi=="L":
                    val+=1
                    if val<l[i]:
                        l[i]="L"
                    elif val>l[i]:
                        l[i]="R"
                    else:
                        l[i]="."
                else:
                    if l[i]==N+1:
                        l[i]="."
                    else:
                        l[i]="R"

        return "".join(l)
