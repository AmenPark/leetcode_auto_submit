class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        N=len(word)
        if numFriends==1:
            return word
        def getch(i):
            if i<N:
                return word[i]
            else:
                return "0"
        tgL = N-numFriends+1
        p = range(N)
        k=0
        for _ in range(tgL):
            maxwd = "0"
            np = []
            for i in p:
                ch=getch(i+k)
                if ch>maxwd:
                    maxwd=ch
                    np=[i]
                elif ch==maxwd:
                    np.append(i)
            if len(np)==1:
                break
            p=np
            k+=1
        return word[np[0]:np[0]+tgL]
    