class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        emp = 0
        while numBottles:
            ans += numBottles
            emp += numBottles
            numBottles = 0
            if emp >= numExchange:
                emp -= numExchange
                numExchange += 1
                numBottles += 1
        return ans