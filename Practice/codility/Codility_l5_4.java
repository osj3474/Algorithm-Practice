class Codility_l5_4 {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int N = A.length;
        if(N == 2){
            // System.out.println(1);
            return 0;
        }

        float min = Integer.MAX_VALUE;
        int answer = 0;
        for(int i=0; i<N-2; i++){
            float two = (A[i]+A[i+1])/2f;
            float three = (A[i]+A[i+1]+A[i+2])/3f;

            float temp = Math.min(two, three);
            if(min > temp){
                min = temp;
                answer = i;
            }
        }
        if(min > (A[N-2]+A[N-1])/2f){
            answer = N-2;
        }
        // System.out.println(answer);
        return answer;
    }
}

