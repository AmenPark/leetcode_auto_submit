class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        where=[0]*((N:=len(mat))*(M:=len(mat[0]))+1)
        for i,row in enumerate(mat):
            for j,val in enumerate(row):
                where[val]=(i,j)
        rflag=[0]*N
        cflag=[0]*M
        for ans, v in enumerate(arr):
            i,j=where[v]
            rflag[i]+=1
            cflag[j]+=1
            if rflag[i]==M or cflag[j]==N:
                return ans
        return -1