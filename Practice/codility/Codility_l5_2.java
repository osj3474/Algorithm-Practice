class Codility_l5_2 {
    public int solution(int A, int B, int K) {
        // write your code in Java SE 8
        int i=A;
        int plus = 0;
        for(; i<B+1; i++){
            if(i%K == 0){
                plus = 1;
                break;
            }
        }
        return (B-i)/K + plus;
    }
}
