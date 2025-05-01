class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        return sum(map(lambda x:x//k, candies))