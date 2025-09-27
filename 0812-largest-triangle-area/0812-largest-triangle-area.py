class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans=0
        N=len(points)
        for i in range(N):
            a1,b1 = points[i]
            for j in range(i):
                a2,b2 = points[j]
                for k in range(j):
                    a3,b3 = points[k]
                    ans=max(ans, abs(a1*b2+a2*b3+a3*b1 - a1*b3-a3*b2-a2*b1)/2)
        return ans