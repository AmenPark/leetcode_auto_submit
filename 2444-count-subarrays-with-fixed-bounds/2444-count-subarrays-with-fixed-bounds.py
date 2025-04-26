import heapq
class Solution:
    def ctSub(self,nums,minK,maxK):
        maxH = []
        minH = []
        N=len(nums)
        d={}
        j=0
        i=0
        flag = True
        ans = 0
        while i<N:
            if flag:
                n=nums[i]
                d[n] = d.get(n,0)+1
                heapq.heappush(maxH,-n)
                heapq.heappush(minH,n)
                while d[-maxH[0]] == 0:
                    heapq.heappop(maxH)
                while d[minH[0]] == 0:
                    heapq.heappop(minH)
                i+=1
                if -maxH[0] >= maxK and minH[0] <= minK:
                    flag = False
            else:
                ans += N-(i-1)
                n = nums[j]
                d[n] -= 1
                while d[-maxH[0]] == 0:
                    heapq.heappop(maxH)
                    if not maxH:
                        break
                while d[minH[0]] == 0:
                    heapq.heappop(minH)
                    if not minH:
                        break
                if not maxH:
                    flag=True
                elif -maxH[0] >= maxK and minH[0] <= minK:
                    flag = False
                else:
                    flag= True
                j+=1
        while j<N:
            if not flag:
                ans += 1
                n = nums[j]
                d[n] -= 1
                while d[-maxH[0]] == 0:
                    heapq.heappop(maxH)
                    if not maxH:
                        break
                while d[minH[0]] == 0:
                    heapq.heappop(minH)
                    if not minH:
                        break
                if not maxH:
                    flag=True
                elif -maxH[0] >= maxK and minH[0] <= minK:
                    flag = False
                else:
                    flag= True
                j+=1
            else:
                break
        return ans
            
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans= self.ctSub(nums, minK, maxK) - self.ctSub(nums, minK-1, maxK) - self.ctSub(nums, minK, maxK+1) + self.ctSub(nums, minK-1, maxK+1)
        return ans