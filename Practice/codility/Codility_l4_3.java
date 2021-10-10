public class Codility_l4_3 {
    public int[] solution(int N, int[] A) {
        // write your code in Java SE 8
        int[] ck = new int[N];
//        Arrays.fill(ck, 0);   // 초기화 까먹지 말기.

        int _max = 0;
        int _min = 0;
        for(int n:A){
            if(n==N+1){
//                for(int i=0; i<N; i++){  // 이걸로 시간초과가 난다.
//                    ck[i] = _max;
//                }
                _min = _max;

            }else{
                int idx = n-1;
                if(ck[idx] < _min){
                    ck[idx] = _min+1;
                }else{
                    ck[idx] += 1;
                }
                if(_max < ck[idx]){
                    _max = ck[idx];
                }
            }
        }
        for(int i=0; i<N; i++){
            if(ck[i]<_min){
                ck[i] = _min;
            }
        }

        return ck;
    }
}