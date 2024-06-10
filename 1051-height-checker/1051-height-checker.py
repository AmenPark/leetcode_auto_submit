class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len([x for x,y in zip(heights, sorted(heights)) if x!=y])