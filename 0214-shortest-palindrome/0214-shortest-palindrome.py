class Solution:
    def shortestPalindrome(self, s: str) -> str:
        fails = [0]
        def addfails():
            i=1
            j=0
            yield
            while True:
                if s[i]==s[j]:
                    fails.append(j+1)
                    i+=1
                    j+=1
                    yield
                elif j:
                    j=fails[j-1]
                else:
                    fails.append(0)
                    i+=1
                    yield
        cfails = addfails()
        j=0
        i=len(s)-1
        while i>j:
            if j>=len(fails):
                next(cfails)
            while True:
                if s[i]==s[j]:
                    i-=1
                    j+=1
                    break
                elif j:
                    j=fails[j-1]
                else:
                    i-=1
                    break
        if i==j-1:
            l=j*2
        else:
            l=i*2+1
        return s[l:][::-1] + s