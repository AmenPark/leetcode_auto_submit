class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        d = deque([i for i in range(1,n+1)])
        while len(d)>1:
            for _ in range(k-1):
                v=d.popleft()
                d.append(v)
            d.popleft()
        return d[0]