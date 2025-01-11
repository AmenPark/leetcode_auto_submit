class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        N=len(people)
        ans = [[] for _ in range(N)]
        people.sort(key = lambda x:(x[0],-x[1]))
        for h,kk in people:
            k = kk
            i=0
            while True:
                if ans[i]:
                    i+=1
                    continue
                if k==0:
                    break
                k-=1
                i+=1
            ans[i] = [h,kk]
        return ans