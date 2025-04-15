class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        arr = [0]*n
        ssum = (n*(n-1))//2
        ct=n
        for _,b in edges:
            if arr[b]==1:
                continue
            arr[b]=1
            ct-=1
            ssum-=b
        if ct==1:
            return ssum
        return -1