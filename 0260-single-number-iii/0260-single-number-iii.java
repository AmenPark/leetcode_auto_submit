class Solution {
    public int[] singleNumber(int[] nums) {
        int xors = 0;
        for(int n:nums){
            xors^=n;
        }
        int bit=xors&(-xors);
        int[] ans={0,0};
        for(int n:nums){
            if((bit&n)==0){
                ans[0]^=n;
            }else{
                ans[1]^=n;
            }
        }
        return ans;
    }
}