class Solution:
    def shortestPalindrome(self, s: str) -> str:
        fails = [0]
        j=0
        i=len(s)-1
        while i>j:
            k=fails[-1]
            while j>=len(fails):
                if s[k] == s[j]:
                    fails.append(fails[k]+1)
                elif k>0:
                    k=fails[k-1]
                else:
                    fails.append(0)
            while True:
                if s[i]==s[j]:
                    j+=1
                    i-=1
                    break
                elif j>0:
                    j=fails[j-1]
                else:
                    i-=1
                    break
        if i==j-1:
            l = j*2
        else:
            l = i*2 + 1
        return s[l:][::-1] + s
                    
        