// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Codility_l6_2 {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int N = A.length;
        if(N==3) return A[0]*A[1]*A[2];

        Arrays.sort(A);

        int answer = Integer.MIN_VALUE;
        int temp = 0;
        for(int i=N; i>2; i--){
            temp = A[i-3]*A[i-2]*A[i-1];
            if(answer < temp){
                answer = temp;
                break;
            }
        }

        if(A[1]<0){
            answer = Math.max(answer, A[0]*A[1]*A[N-1]);
        }

        return answer;

    }
}
