class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = {}
        atoms = set()
        ans = 0
        for i, num in enumerate(arr):
            for j in range(i):
                if arr[j] >= (num+1)//2:
                    break
                if num-arr[j] in atoms:
                    k=num-arr[j]
                    dp[(num, k)] = max(dp.get((num,k),0), dp.get((k, arr[j]),0)+1)
                    ans=max(ans, dp[(num,k)])
            atoms.add(num)
        return ans and ans+2
            
