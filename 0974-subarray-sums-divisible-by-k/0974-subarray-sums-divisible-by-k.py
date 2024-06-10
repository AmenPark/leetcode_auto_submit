class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ss={0:1}
        s=0
        for n in nums:
            s+=n
            s%=k
            ss[s]=ss.get(s,0)+1
        ans = 0
        for _,n in ss.items():
            ans += (n-1)*n//2
        return ans
    