class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        N=len(s)
        if N%2:
            return False
        ct=0
        for c,v in zip(s,locked):
            if v=="1" and c=="(":
                ct+=1
        ct=(N//2) - ct
        depth = 0
        for c,v in zip(s,locked):
            if v=="1":
                if c=="(":
                    depth += 1
                else:
                    depth -= 1
            elif ct:
                depth+=1
                ct-=1
            else:
                depth-=1
            if depth<0:
                return False
        if depth==0:
            return True
        return False