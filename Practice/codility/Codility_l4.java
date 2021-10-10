import java.util.*;

public class Codility_l4 {
    public static void main(String args[]) {
        int[] A = {1,3,1,4,2,3,5,4};
        int X = 5;

        int N = A.length;
        boolean flag = false;
        HashSet<Integer> s = new HashSet<>();
        int i=0;
        for(;i<N;i++){
            s.add(A[i]);
            if(s.size()==X){
                flag = true;
                break;
            }
        }
        if(flag){
            System.out.println(i);
        }else{
            System.out.println(-1);
        }
    }
}


