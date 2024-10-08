class Solution:
    def minSwaps(self, s: str) -> int:
        minct = 0
        ct = 0
        for ch in s:
            if ch == "[":
                ct+=1
            else:
                ct-=1
            minct = min(minct,ct)
        return (-minct-1)//2 + 1