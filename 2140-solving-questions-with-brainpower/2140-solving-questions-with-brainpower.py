class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N=len(questions)
        dp = [0]*(N+1)
        for i,(pt,pow) in enumerate(questions):
            tg = min(i+pow+1,N)
            dp[tg] = max(dp[tg], dp[i]+pt)
        print(dp)

        return dp[N]
        