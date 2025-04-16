class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        s=0
        cts = [1,0]
        for n in arr:
            s+=n
            cts[s%2] +=1
        return (cts[0]*cts[1]) % (10**9 + 7)