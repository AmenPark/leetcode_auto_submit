class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l=[0]*len(s)
        bch = "a"
        for i,ch in enumerate(s):
            l[i] = ord(ch)-ord(bch)
            bch = ch
        l.append(0)
        for x,y,z in shifts:
            if z:
                l[x]+=1
                l[y+1]-=1
            else:
                l[x]-=1
                l[y+1]+=1
        l.pop()
        ss =0
        ans = []
        for v in l:
            ss+=v
            ss%=26
            ans.append(chr(97+ss))
        return "".join(ans)