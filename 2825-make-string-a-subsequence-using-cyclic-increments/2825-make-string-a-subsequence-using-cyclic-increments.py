class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        N=len(str2)
        j=0
        for ch in str1:
            if (ord(str2[j]) - ord(ch))%26 <=1:
                j+=1
            if j==N:
                return True
        return False