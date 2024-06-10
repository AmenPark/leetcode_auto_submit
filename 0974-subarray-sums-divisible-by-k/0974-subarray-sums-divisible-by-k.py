class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ss=[0]*k
        s=0
        for n in nums:
            s+=n
            s%=k
            ss[s]+=1
        ss[0]+=1
        ans = 0
        for n in ss:
            ans += (n-1)*n//2
        return ans
    
#    0 4 4 4 2 4 0