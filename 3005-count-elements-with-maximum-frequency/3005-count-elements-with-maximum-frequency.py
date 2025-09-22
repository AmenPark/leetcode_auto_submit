class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mcf = 0
        mcct = 0
        cts = {}
        for n in nums:
            cts[n] = cts.get(n,0)+1
            if cts[n] > mcf:
                mcf = cts[n]
                mcct = 1
            elif cts[n] == mcf:
                mcct += 1
        return mcct * mcf