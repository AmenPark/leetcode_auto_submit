class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N=len(boxes)
        ans=[0]*N
        for to_do in [range(N), range(N-1,-1,-1)]:
            ss=0
            val=0
            for i in to_do:
                val += ss
                ans[i] +=val
                ss+=int(boxes[i]=="1")
        return ans
        