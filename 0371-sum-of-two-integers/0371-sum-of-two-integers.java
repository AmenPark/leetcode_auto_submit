class Solution {
    public int getSum(int a, int b) {
        int c;
        while (b!=0){
            c=a^b;
            b&=a;
            a=c;
            b<<=1;
        }
        return a;
    }
}