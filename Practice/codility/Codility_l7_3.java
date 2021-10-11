// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Codility_l7_3 {
    public int solution(String S) {
        // write your code in Java SE 8
        Stack<Character> st = new Stack<>();
        boolean flag = false;

        for (int i = 0; i < S.length(); i++) {
            char now = S.charAt(i);
            if(now==')'){
                if( st.isEmpty() || st.peek() != '(') {
                    flag = true;
                    break;
                }
                st.pop();
            }else{
                st.add(now);
            }
        }

        if(flag || !st.isEmpty()){
            return 0;
        }
        return 1;
    }
}
