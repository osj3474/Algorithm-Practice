//  큐 자료구조 사용했을 때 => 시간 초과
import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayDeque<Integer> q = new ArrayDeque<Integer>();

        for(int i=0; i<N; i++) {
            String cmd = sc.next();
            if(cmd.equals("push")){
                q.add(sc.nextInt());
            }else if(cmd.equals("pop")){
                if(q.isEmpty()){
                    System.out.println(-1);
                }else{
                    System.out.println(q.poll());
                }
            }else if(cmd.equals("size")){
                System.out.println(q.size());
            }else if(cmd.equals("empty")){
                if(q.isEmpty()){
                    System.out.println(1);
                }else{
                    System.out.println(0);
                }
            }else if(cmd.equals("front")){
                if(q.isEmpty()){
                    System.out.println(-1);
                }else{
                    System.out.println(q.peek());
                }
            }else if(cmd.equals("back")){
                if(q.isEmpty()){
                    System.out.println(-1);
                }else{
                    System.out.println(q.peekLast());
                }
            }
        }
    }
}

// ===== 답지인데도 시간 초과,,  ======
//
//import java.util.*;
//
//public class Main {
//    public static void main(String args[]) {
//        Scanner sc = new Scanner(System.in);
//        int N = sc.nextInt();
//        int[] q = new int[10001];
//        int begin = 0;
//        int end = 0;
//
//        for(int i=0; i<N; i++) {
//            String cmd = sc.next();
//            if(cmd.equals("push")){
//                q[end++] = sc.nextInt();
//            }else if(cmd.equals("pop")){
//                if(begin == end){
//                    System.out.println("-1");
//                }else{
//                    System.out.println(q[begin++]);
//                }
//            }else if(cmd.equals("size")){
//                System.out.println(end-begin);
//            }else if(cmd.equals("empty")){
//                if(begin == end){
//                    System.out.println("1");
//                }else{
//                    System.out.println("0");
//                }
//            }else if(cmd.equals("front")){
//                if(begin == end){
//                    System.out.println("-1");
//                }else{
//                    System.out.println(q[begin]);
//                }
//            }else if(cmd.equals("back")){
//                if(begin == end){
//                    System.out.println("-1");
//                }else{
//                    System.out.println(q[end-1]);
//                }
//            }
//        }
//    }
//}

