// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Codility_l7_2 {
    public int solution(int[] A, int[] B) {
        // write your code in Java SE 8
        int N = A.length;
        int alive = N;

        Stack<Integer> st = new Stack<>();
        int now;
        for (int i = 0; i < N; i++) {
            if(B[i] == 1){
                st.add(i);
            }else{
                while(!st.isEmpty()){
                    now = st.peek();
                    if(A[now] < A[i]){
                        alive -= 1;
                        st.pop();
                    }else{
                        alive -= 1;
                        break;
                    }
                }
            }
        }
        return alive;
    }
}