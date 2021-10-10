class Codility_l5_1 {
    static int MAX = 1000000000;
    public int solution(int[] A) {
        // write your code in Java SE 8
        int total = 0;
        for(int n:A){
            if(n==1){
                total += 1;
            }
        }

        int answer = 0;
        for(int n:A){
            if(n==0){
                answer += total;
                if(answer > MAX){
                    answer = -1;
                    break;
                }
            }else{
                total -= 1;
            }
        }

        // System.out.println(answer);
        return answer;
    }
}
