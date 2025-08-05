class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        M=len(baskets)
        for f in fruits:
            for i in range(M):
                if f<=baskets[i]:
                    baskets[i]=0
                    break
        return len([b for b in baskets if b!=0])