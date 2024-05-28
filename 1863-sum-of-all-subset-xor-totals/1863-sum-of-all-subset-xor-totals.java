class Solution {
    public int subsetXORSum(int[] nums) {
        int t = 0;
        for(int n:nums){
            t|=n;
        }
        return t<<(nums.length-1);
    }
}