class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        d={}
        for n in nums1:
            d[n] = d.get(n,0)+1
        for n in nums2:
            if d.get(n,0):
                d[n] -= 1
                ans.append(n)
        return ans