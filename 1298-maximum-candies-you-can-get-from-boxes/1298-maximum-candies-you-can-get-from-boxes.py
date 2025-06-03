class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ans =0
        boxs = []
        for box in initialBoxes:
            if status[box]==1:
                boxs.append(box)
            else:
                status[box]=2

        while boxs:
            nboxs = []
            for box in boxs:
                ans += candies[box]
                for k in keys[box]:
                    if status[k]==2:
                        nboxs.append(k)
                    status[k]=1
                for cb in containedBoxes[box]:
                    if status[cb]==1:
                        nboxs.append(cb)
                    else:
                        status[cb]=2
            boxs=nboxs
        return ans