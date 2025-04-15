class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        subsum = 0
        deq = deque()
        length = 0
        ans = 1000000
        N = len(nums)
        i=0
        while i<N:
            if subsum >= k:
                ans=min(ans,length)
                fraglen, fragval = deq.popleft()
                length -= fraglen
                subsum -= fragval
                continue
            if nums[i]>0:
                subsum += nums[i]
                deq.append((1,nums[i]))
                length += 1
                i+=1
            else:
                subsum += nums[i]
                length += 1
                if subsum<=0:
                    subsum=0
                    deq=deque()
                    length=0
                    i+=1
                else:
                    val = nums[i]
                    l=1
                    while val < 0:
                        fl, fv = deq.pop()
                        l+=fl
                        val+=fv
                    deq.append((l,val))
                    i+=1
        while subsum >=k:
            ans=min(ans,length)
            if not deq:
                break
            fl, fv = deq.popleft()
            length -= fl
            subsum -= fv
        if ans==1000000:
            return -1
        return ans
