class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l=0
        for n in arr:
            if n%2:
                l+=1
                if l==3:
                    return True
            else:
                l=0
        return False