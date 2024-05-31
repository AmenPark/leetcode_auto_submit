class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = (w:=reduce(lambda x,y:x^y, nums,0))&-w
        print(n)
        ans=reduce(lambda x,y : [x[0]^y if n&y==0 else x[0], x[1]^y if n&y else x[1]] ,nums,[0,0])
        return ans