class Solution {
    public int numSteps(String s) {
        int ans=0;
        int i=s.length()-1;
        while (s.charAt(i)=='0'){
            ans++;
            i--;
        }
        if(i==0) return ans;
        while (i>=0){
            if (s.charAt(i)=='1'){
                ans++;
                i--;
                continue;
            }
            while (s.charAt(i)=='0'){
                ans+=2;
                i--;
            }
        }
        return ans+1;

    }
}