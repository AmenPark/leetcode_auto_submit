class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ls = [(x,i) for i,(x,y) in enumerate(intervals)]
        ls.sort()
        ans = []
        # print(ls)
        for _,y in intervals:
            m=0
            M=len(ls)-1
            if ls[-1][0]<y:
                ans.append(-1)
                continue
            if ls[0][0]==y:
                ans.append(0)
                continue
            while m<M-1:
                mid = (m+M)//2
                if ls[mid][0]>=y:
                    M=mid
                else:
                    m=mid
            # print(y,m,M)
            ans.append(ls[M][1])
        return ans