class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ct = {}
        for ans in answers:
            ct[ans] = ct.get(ans,0)+1
        rt = 0
        for k,v in ct.items():
            rt += ((v-1)//(k+1) + 1) * (k+1)
        return rt