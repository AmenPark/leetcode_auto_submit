class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 1 + (abs(x-z)>abs(y-z)) - (abs(x-z)==abs(y-z))