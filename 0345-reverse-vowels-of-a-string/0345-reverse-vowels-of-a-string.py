class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        v=[]
        vowels=set("aeiouAEIOU")
        for i,x in enumerate(s):
            if x in vowels:
                v.append(i)
                l.append(0)
            else:
                l.append(x)
        for a,b in zip(v,v[::-1]):
            l[a] = s[b]
        return "".join(l)
        