class Solution {
    public int subsetXORSum(int[] nums) {
        int N = nums.length;
        int t = 0;
        for(int n:nums){
            t|=n;
        }
        return t<<(N-1);
    }
}