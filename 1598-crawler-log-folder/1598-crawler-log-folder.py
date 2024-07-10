class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s=0
        for log in logs:
            if log=="../":
                s=max(0,s-1)
            elif log=="./":
                continue
            else:
                s+=1
        return s