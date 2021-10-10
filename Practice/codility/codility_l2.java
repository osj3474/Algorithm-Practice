import java.util.*;

class Codility_l2 {
    public int solution(int[] A) {
        // 1차 방법

//        HashMap<Integer, Integer> map = new HashMap<>();
//        for(int n: A){
//            map.computeIfPresent(n, (k, v)-> v^1);
//            map.putIfAbsent(n, 1);
//        }
//
//        int answer = 0;
//        for (Map.Entry<Integer, Integer> e : map.entrySet()) {
//            if(e.getValue()==1){
//                answer = e.getKey();
//                break;
//            }
//        }
//        return answer;


        // 2차 방법 : xor하면, 결국 교환법칙으로 하나만 남는구나.
        int N = A.length;
        int answer = A[0];
        for(int i=1; i<N; i++){
            answer = answer ^ A[i];
        }
        return answer;
    }
}