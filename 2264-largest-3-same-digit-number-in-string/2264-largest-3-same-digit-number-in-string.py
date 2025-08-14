class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max([str(i)*3 for i in range(10) if str(i)*3 in num]+[""])