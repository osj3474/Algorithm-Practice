// you can also use imports, for example:

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Codility_l5_3 {
    static int[][] dic;
    public int[] solution(String S, int[] P, int[] Q) {
        // write your code in Java SE 8

        int N = P.length;
        int s_len = S.length();

        dic = new int[4][s_len+1];
        for(int i=0; i<s_len; i++){
            char now = S.charAt(i);
            int idx = i+1;
            for(int j=0; j<4; j++){
                dic[j][idx] = dic[j][i];
            }

            if('A'==now){
                dic[0][idx] += 1;
            }else if('C'==now){
                dic[1][idx] += 1;
            }else if('G'==now){
                dic[2][idx] += 1;
            }else{
                dic[3][idx] += 1;
            }


        }

        int[] answer = new int[N];
        for(int i=0; i<N; i++){
            int s = P[i];
            int e = Q[i]+1;
            int j=0;
            if(s==e){
                for(; j<4; j++){
                    if(dic[j][e]!=dic[j][s]){
                        break;
                    }
                }
            }else{
                for(; j<4; j++){
                    if(dic[j][e]-dic[j][s] > 0){
                        break;
                    }
                }
            }

            answer[i] = j+1;
            if(j==4){ answer[i] -= 1;}
        }

        return answer;
    }
}