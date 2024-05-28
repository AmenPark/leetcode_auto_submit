class Solution {
    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        int N = nums.length;
        int j=N;
        for(int i=0;i<N;i++){
            if(nums[i]>=N-i){
                if(i==0) return j;
                if(nums[i-1]<j) return j;
                return -1;
            }
            j--;
        }
        return -1;
    }
}