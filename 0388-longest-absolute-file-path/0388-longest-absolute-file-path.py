class Solution:
    def lengthLongestPath(self, input: str) -> int:
        l=input.split("\n")
        nl = [(len(path) - (w:=len(path.lstrip("\t"))), w+1, "." in path) for path in input.split("\n")]
        stack = []
        nsum=0
        ans=1
        print(nl)
        for p,x,tf in nl:
            while p<len(stack):
                nsum -= stack.pop()
            nsum+=x
            stack.append(x)
            if tf==True:
                ans=max(ans,nsum)
        return ans-1
