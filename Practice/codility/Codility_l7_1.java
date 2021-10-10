// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Codility_l7_1 {
    public int solution(String S) {
        // write your code in Java SE 8
        Stack<Character> s = new Stack<>();

        boolean flag = false;
        for(int i=0; i<S.length(); i++){
            char now = S.charAt(i);
            if(now == ')'){
                try{
                    if(s.pop() != '('){
                        flag = true;
                        break;
                    }
                }catch (Exception e){
                    flag = true;
                    break;
                }

            }else if(now == '}'){
                try{
                    if(s.pop() != '{'){
                        flag = true;
                        break;
                    }
                }catch (Exception e){
                    flag = true;
                    break;
                }
            }else if(now == ']'){
                try{
                    if(s.pop() != '['){
                        flag = true;
                        break;
                    }
                }catch (Exception e){
                    flag = true;
                    break;
                }
            }else{
                s.add(now);
            }
        }

        if(flag || s.size()>0){
            return 0;
        }
        return 1;



    }
}
