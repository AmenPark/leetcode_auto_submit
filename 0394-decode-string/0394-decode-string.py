class Solution:
    def decodeString(self, s: str) -> str:
        l = iter(s)
        def decode(it, iternum):
            nch = next(it, "")
            string = []
            num=0
            while nch:
                if nch=="]":
                    return ("".join(string))*iternum
                elif nch=="[":
                    string.append(decode(it, max(1,num)))
                    num=0
                elif nch.isdigit():
                    num*=10
                    num+=int(nch)
                else:
                    string.append(nch)                    
                nch=next(it,"")
            return ("".join(string))*iternum
        return decode(l,1)
                