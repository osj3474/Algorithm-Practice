class Codility_l3 {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int N = A.length;
        int rightSum = 0;
//        Arrays.stream(A).sum() - A[0];  // stream으로 sum 구하지 말기.
        for(int i=1; i<N; i++){
            rightSum += A[i];
        }
        int leftSum = A[0];

        int _min = Integer.MAX_VALUE;
        for(int i=1; i<N; i++){
            int dif = Math.abs(leftSum-rightSum);
            if(_min > dif){
                _min = dif;
            }
            leftSum += A[i];
            rightSum -= A[i];
        }
        return _min;
    }
}