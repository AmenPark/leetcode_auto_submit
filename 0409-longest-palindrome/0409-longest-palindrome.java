class Solution {
    public int longestPalindrome(String s) {
        int[] cts=new int['z'-'A'+1];
        for(char ch:s.toCharArray()){
            cts[ch-'A']+=1;
        }
        int ans=0;
        int odd = 0;
        for(int i:cts){
            ans += i&(-2);
            odd += 1&i;
        }
        if (odd>0){
            ans++;
        }
        return ans;
    }
}