// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Codility_l4_2 {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int _max = Integer.MIN_VALUE;

        HashSet<Integer> s = new HashSet<>();
        for(int n:A){
            if(_max < n) {
                _max = n;
            }
            s.add(n);
        }
        if(s.size()==_max){
            return 1;
        }
        return 0;

    }
}