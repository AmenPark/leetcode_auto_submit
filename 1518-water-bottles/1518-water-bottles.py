class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return ((numBottles-1)//(numExchange-1))+numBottles