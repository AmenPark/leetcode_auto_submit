class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int N=s.length();
        int[] arr = new int[N+1];
        int temp = 0;
        for(int i=0;i<N;i++){
            temp += Math.abs(s.charAt(i) - t.charAt(i));
            arr[i+1]=temp;
        }
        int i=0,j=1,ans=0;
        while(j<N+1){
            if(arr[j]-arr[i]<=maxCost){
                if(ans<j-i) ans=j-i;
                j++;
            }else{
                i++;
            }
        }
        return ans;
    }
}