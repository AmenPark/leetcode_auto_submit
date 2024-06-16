class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = [nums[0]]
        p=0
        for n in nums:
            if n == ans[-1]:
                continue
            if n>ans[-1]:
                if p==1:
                    ans[-1]=n
                else:
                    p=1
                    ans.append(n)
            elif n<ans[-1]:
                if p==-1:
                    ans[-1]=n
                else:
                    p=-1
                    ans.append(n)
        return len(ans)