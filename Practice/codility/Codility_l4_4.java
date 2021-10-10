// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Codility_l4_4 {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int _max = Integer.MIN_VALUE;
        for(int n:A){
            if(_max < n){
                _max = n;
            }
        }
        int N = _max;
        boolean[] ck = new boolean[N+1];
        Arrays.fill(ck, true);
        for(int n:A){
            if(n<0){
                continue;
            }
            ck[n] = false;
        }
        int i=1;
        for(; i<=N; i++){
            if(ck[i]){
                break;
            }
        }
        return i;
    }
}
