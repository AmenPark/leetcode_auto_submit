class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int s=1;
        ArrayList<Integer> l = new ArrayList<>();
        for(int n:nums){
            if(n%2==1){
                l.add(s);
                s=1;
            }else s++;
        }
        l.add(s);
        int ans=0;
        for(int i=k;i<l.size();i++){
            ans+=l.get(i)*l.get(i-k);
        }
        return ans;
    }
}
