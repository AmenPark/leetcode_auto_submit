class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        N=len(customers)
        nt=0
        stsum=0
        etsum=0
        for x,y in customers:
            stsum += x
            if nt<=x:
                nt=x
            nt += y
            etsum+=nt
        return (etsum-stsum)/N