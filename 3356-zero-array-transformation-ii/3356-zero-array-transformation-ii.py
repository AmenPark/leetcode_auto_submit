class Node:
    def __init__(self,nums, l, r):
        self.l=l
        self.r=r
        self.lazy = 0
        if r==l+1:
            self.left=None
            self.right=None
            self.val=nums[l]
        else:
            m=(l+r)//2
            self.left=Node(nums,l,m)
            self.right=Node(nums,m,r)
            self.val=max(self.left.val, self.right.val)
    def getMaxValue(self):
        return self.val - self.lazy
    def decrese(self, l, r, dec):
        if l<=self.l and r>=self.r:
            self.lazy += dec
            return
        self.left.lazy += self.lazy
        self.right.lazy += self.lazy
        if l >= self.left.r:
            self.right.decrese(l,r,dec)
        elif r<=self.right.l:
            self.left.decrese(l,r,dec)
        else:
            self.left.decrese(l, self.left.r, dec)
            self.right.decrese(self.right.l, r, dec)
        self.lazy=0
        self.val = max(self.left.getMaxValue(), self.right.getMaxValue())
            

        
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        root = Node(nums, 0, len(nums))
        if root.getMaxValue()==0:
            return 0
        for i, (l,r,v) in enumerate(queries,1):
            root.decrese(l,r+1,v)
            if root.getMaxValue()==0:
                return i
        return -1