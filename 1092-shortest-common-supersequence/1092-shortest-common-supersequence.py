class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def createfails(l):
            rt=[0]*len(l)
            j=0
            for i,ch in enumerate(l[1:],1):
                while j>0 and ch!=l[j]:
                    j=rt[j-1]
                if ch==l[j]:
                    rt[i]=j+1
                    j+=1
            return rt
        fails1 = createfails(str1)
        fails2 = createfails(str2)
        idx=0
        for ch in str1:
            while idx and ch!=str2[idx]:
                idx=fails1[idx-1]
            if ch==str2[idx]:
                idx+=1
        
        idx2=0
        for ch in str2:
            while idx2 and ch!=str1[idx2]:
                idx2=fails2[idx2-1]
            if ch==str1[idx2]:
                idx2+=1
        if idx>idx2:
            return str1+str2[idx:]
        elif idx2>idx:
            return str2+str1[idx2:]
        return str1+str2[idx:]