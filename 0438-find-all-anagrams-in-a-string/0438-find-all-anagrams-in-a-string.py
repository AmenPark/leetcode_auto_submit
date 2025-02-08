class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = {}
        ans=[]
        for ch in p:
            d[ch]=d.get(ch,0)+1
        flag=len(d)
        N=len(p)
        sidx = 0
        for ch in s:
            d[ch] = d.get(ch,0) - 1
            if d[ch]==-1:
                flag += 1
            elif d[ch]==0:
                flag -= 1
            N -= 1
            if N<0:
                dch = s[sidx]
                d[dch] += 1
                if d[dch]==0:
                    flag -=1
                elif d[dch] == 1:
                    flag +=1
                N+=1
                sidx+=1
            if flag==0:
                ans.append(sidx)
        return ans
