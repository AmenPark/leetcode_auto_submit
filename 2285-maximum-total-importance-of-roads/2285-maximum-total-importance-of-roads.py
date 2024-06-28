class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        conn_num = [0]*n
        for x,y in roads:
            conn_num[x]+=1
            conn_num[y]+=1
        conn_num.sort()
        ans=0
        for i,n in  enumerate(conn_num,1):
            ans += i*n
        return ans