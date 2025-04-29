class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cases = [True]*501
        for n in nums:
            cases[n] = not cases[n]
        return all(cases)