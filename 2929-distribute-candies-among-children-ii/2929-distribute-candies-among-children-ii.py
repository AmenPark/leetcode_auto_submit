class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n>limit*3:
            return 0
        # (n+2) choose 2 : n을 3명에게 나눔
        # (n+2 - limit-1) choose 2: limit+1만큼 첫번째 사람에게 주고 나눔
        def choose2(x):
            if x<0:
                return 0
            return (x*(x-1))//2
        ans = choose2(n+2) - 3*choose2(n+2 - limit-1) + 3*choose2(n+2 - limit*2 - 2) + choose2(n+2 - limit*3 - 3)
        return ans