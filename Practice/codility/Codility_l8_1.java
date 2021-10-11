// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Codility_l8_1 {
    public int solution(int[] A) {
        // write your code in Java SE 8
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();

        int max = Integer.MIN_VALUE;
        int idx = -1;
        for(int i=0; i<A.length; i++){
            if(! map.containsKey(A[i])){
                map.put(A[i], new ArrayList<Integer>());
            }
            map.get(A[i]).add(i);
            int temp = map.get(A[i]).size();
            if(max < temp) {
                max = temp;
                idx = A[i];
            }
        }
        if(idx == -1 || map.get(idx).size() < A.length/2+1){
            // System.out.println(-1);
            return -1;
        }
        return map.get(idx).remove(0);
    }
}

