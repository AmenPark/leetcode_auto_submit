class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = {}
        ans = 0
        for i,n in enumerate(nums):
            for idx in dic.get(n,[]):
                if (i*idx)%k == 0:
                    ans+=1
            if n not in dic:
                dic[n] = []
            dic[n].append(i)
        return ans