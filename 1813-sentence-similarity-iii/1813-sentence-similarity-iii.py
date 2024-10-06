class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1 = sentence1.split()
        l2 = sentence2.split()
        if len(l1)<len(l2):
            l1,l2 = l2,l1
        N=len(l1)
        M=len(l2)
        i=0
        while l1[i] == l2[i]:
            i+=1
            if i==M:
                return True
        j=-1
        while l1[j]==l2[j]:
            j-=1
            if j==-M-1:
                return True
        if i-j >= M+1:
            return True
        return False