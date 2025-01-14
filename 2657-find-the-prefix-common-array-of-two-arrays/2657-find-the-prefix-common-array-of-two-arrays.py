class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = [0]*len(A)
        ans = [0]*len(A)
        ss=0
        for i,a,b in enumerate(zip(A,B)):
            C[a]+=1
            C[b]+=1
            if C[a]==2:
                ss+=1
            if C[b]==2:
                ss+=1
            ans[i]=ss
        return ans