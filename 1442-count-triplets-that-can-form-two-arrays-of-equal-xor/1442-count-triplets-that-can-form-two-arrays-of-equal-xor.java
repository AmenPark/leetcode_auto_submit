class Solution {
    public int countTriplets(int[] arr) {
        HashMap<Integer,Integer> d1 = new HashMap<>(),d2 = new HashMap<>(),d3 = new HashMap<>();
        int v=0, ans=0, i=0;
        d1.put(0,1);
        d2.put(0,-1);
        d3.put(0,1);
        int t1,t2,t3;
        for(int x:arr){
            v^=x;
            if (d1.containsKey(v)){
                t1=d1.get(v); t2=d2.get(v); t3=d3.get(v);
                ans+=t1+(i-t2-2)*t3;
                d1.put(v,t1+(i-t2)*t3+1);
                d2.put(v,i);
                d3.put(v,t3+1);
            }else{
                d1.put(v,1);d2.put(v,i);d3.put(v,1);
            }
            i++;
        }
        return ans;
    }
}