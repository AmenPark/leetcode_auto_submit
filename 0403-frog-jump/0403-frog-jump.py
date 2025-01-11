class Solution:
    def canCross(self, stones: List[int]) -> bool:
        records = {i:set() for i in stones}
        records[0] = {0}
        for pos in stones:
            for dist in records[pos]:
                for d in range(max(1,dist-1), dist+2):
                    if pos+d in records:
                        records[pos+d].add(d)
        if records[stones[-1]]:
            return True
        return False


