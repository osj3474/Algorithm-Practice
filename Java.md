# 입력

```java
// 입력 (일반 경우)
Scanner sc = new Scanner(System.in);  // ("4.80초")
// EOF까지 입력받기 (입력이 주어지지 않은 경우)
// while(sc.hasNextInt())
sc.next();     // 한 단어 (String)
sc.nextline(); // 한 줄   (String)
sc.nextInt();  // 한 숫자 (Integer)

// 입력 (많은 경우)  이거 쓰게 되면, (throws IOException) 필요
BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // ("0.65초")
br.close(); // main 끝나기 전에 해주기


// (한 줄에) 숫자 1개
int N = Integer.parseInt(br.readLine());  // (String만 가능) + int형 반환
int N = Integer.valueOf(bf.readLine());   // (String, Integer 가능) + Integer형 반환

// (한 줄에) 숫자 2개 이상
String[] nums = br.readLine().split(" ");

// 혹은
StringTokenizer st; 
st = new StringTokenizer(br.readLine());
while(st.countTokens()!=0){
  System.out.println(Integer.parseInt(st.nextToken()));
}

// tokenize
StringTokenizer st;
st = new StringTokenizer(br.readLine());
```



<br />

# 출력

```java
// 출력 (일반 경우)
System.out.println("30.00초");

// 출력 (많은 경우)
// BufferedWriter ("0.95초");
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
bw.close(); // main 끝나기 전에 해주기

// StringBuilder  ("1.18초");
StringBuilder sb = new StringBuilder();


// [조합]
sb.append(answer + "\n");  // 이렇게 쓰고
bw.write(sb.toString());   // 한꺼번에 넣고
bw.close();                // 종료해주고
```





# 파이썬과 비교하기

1. 한줄 입력 받기

   [python]

   ```python
   s = input()
   ```

   [java]

   ```java
   BufferedReader br = new BufferedReader(InputStreamReader(System.in));
   String s = br.readLine();
   ```



2. 입렵받은 한줄 split()하기

   (3개 입력의 가정)

   [python]

   ```
   n, m, l = map(int, s.split())
   ```

   [java]

   ```java
   // main method 밖
   static int n, m, l;
   
   // main method 안
   StringTokenizer st = new StringTokenizer(s, " ");
   n = Integer.parseInt(st.nextToken());
   m = Integer.parseInt(st.nextToken());
   l = Integer.parseInt(st.nextToken());
   ```

   

3. n줄 입력 받기 

   (한 줄에 여러 수들이 있다고 가정)

   [python]

   ```python
   A = [list(map(int, input().split())) for _ in range(n)]
   ```

   [java]

   ```java
   // main method 밖
   static int map[][];
   
   // main method 안
   map = new int[n+1][n+1];
   for(int i=0; i<n+1; i++){
     Arrays.fill(map[i], 0);
   }
   for(int i=0; i<n; i++){
     String s = br.readLine();
     StringTokenizer stt = new StringTokenizer(s, " ");
     int j = 0;
    	while(stt.countTokens()!=0){
       map[i][j] = Integer.parseInt(stt.nextToken());
     }
   }
   ```

   ```java
   // main 밖에 이렇게 해두고
   static int n, m;
   static int[][] a;
   static boolean[][] check;
   static int[][] group;
   
   // 입력 이렇게 받기
   BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
   BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
   String[] st = bf.readLine().split(" ");  // 3 5 이런 입력 받은 거임.
   
   n = Integer.parseInt(st[0]);
   m = Integer.parseInt(st[1]);
   a = new int[n][m];             // 해당 사이즈의 2차원 array 만들기
   
   
   
   // 출력 이렇게 하기
   bw.write(String.valueOf(ans%10));
   ```

   ```java
   // valueOf() 함수는 >>> String 변환
   
   String a = String.valueOf(1, "135", true, ...);  // 어떤 형이든 String으로 바꿈
   
   ```

   
   
4. 형 변환

   [python]

   ```python
   a = 1
   b = '5'
   
   a = int(b)  # str -> int
   b = str(a)  # int -> str
   ```

   [java]

   ```java
   int a = 1;
   String b = '5';
   
   a = Integer.parseInt(b); // str -> int
   b = Integer.toString(a); // int -> str
   
   String S = "nowic";
   System.out.println(S.charAt(2));   // w출력
   S.charAt(1)+"" // char -> str
   ```

   

5. 딕셔너리 사용하기

   [python]

   ```python
   from collections import defaultdict
   
   map = defaultdict();
   map[x] += 1;
   ```

   [java]

   ```java
   HashMap<Integer, Integer> map = new HashMap<>();
   
   if (map.containsKey(x)) {
     int temp = map.get(x);
     map.put(x, temp+1);
   } else {
     map.put(x, 1);
   }
   
   import java.util.Map.Entry;
   for (Entry<Integer, Integer> e : map.entrySet()) {
     v.add(new Pair(e.getKey(), e.getValue()));
   }
   
   
   
   // 새로운
   map.computeIfPresent(1, (key, value) -> ++value);
   map.putIfAbsent(1, 1);
   
   
   HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
   for(int i=0; i<A.length; i++){
     if(! map.containsKey(A[i])){
       map.put(A[i], new ArrayList());
     }
     map.get(A[i]).add(i);
   }
   ```
   
   



6. set 사용하기

   [python]

   ```python
   a = set()
   a.add(30)
   
   if 30 in a:
     print("O(1)")
   ```

   [java]
   
   ```java
   HashSet<Integer> s = new HashSet<>();  // or Set<Integer> set = new HashSet<Integer>();
   
   s.add(1);
   ```
   
   





7. stack, queue

   [python]

   ```python
   from collections import deque
   
   # ====== stack ====== #
   s = []       
   s.append(1)
   s.pop()
   
   # ====== deque ====== #
   q = deque()
   q.append(1)
   q.popleft()
   ```

   [java]

   ```java
   import java.util.*
   
   // ====== stack ====== //
   Stack<Integer> s = new Stack<>();
   s.push(1);
   s.pop();
   s.peek();
   s.size();
   s.empty();    // 비우기
   s.isEmpty();  // 비었는지 확인
   
     
     
   // ====== queue ====== //
   Queue<Integer> q = new LinkedList<Integer>();
   // [넣기]
   q.add(1);
   // [꺼내기]
   q.peek();    // 맨 위 값 보기
   q.poll();    // 꺼냄 (없으면 null)
   q.remove();  // 꺼냄 (없으면 에러!)
   q.clear();   // 초기화
   // [속성]
   q.size();
   q.isEmpty();
   q.contains(1); // 값이 있는지 확인
   
   
   // ====== deque ====== //
   ArrayDeque<Integer> q = new ArrayDeque<Integer>();
   // [넣기]
   q.add(1);    // (원래 방향) 넣기
   q.push(2);   // (반대 방향) 넣기
   // [꺼내기]
   q.peek();      // (원래 방향) 맨 위 값 보기
   q.pop();       // (원래 방향) 꺼냄 (없으면 null)
   q.poll();      // (원래 방향) 꺼냄 (없으면 null)
   q.remove();    // (원래 방향) 꺼냄 (없으면 에러!)
   
   q.peekLast();  // (원래 방향) 맨 위 값 보기
   q.pollLast();  // (반대 방향) 꺼냄 (없으면 null)
   
   q.clear();   // 초기화
   // [속성]
   q.isEmpty();
   ```

   

8. 반복문

   [python]

   ```python
   for num in [n+1, n+2, n+3]:
     print(num)
   ```

   

   [java]

   ```java
   for (int num : new int[]{n+1, n+2, n+3}){
     System.out.println(num);
   }
   ```

   



9. List

   [python]

   ```python
   final DevEvent devEvent = devEventQueryRepository.findDevEventById(id)
                   .orElseThrow(() -> new DevEventNotFoundException(ErrorCode.DEV_EVENT_NOT_FOUND));
   ```
   
   
   
   [java]
   
   ```java
   ArrayList<Integer> first = new ArrayList<>();
   
   
   ```
   
   ```java
   // 배열 출력
   System.out.println(Arrays.toString(arr));
   ```
   
   





10. null 체크

    ```java
    // null 체크
    String ck = String.valueOf(something);
    if("null".equals(ck)) {
        
    }
    ```

    



11. dfs / bfs 관용

    ```java
    final static int[] dx = {0,0,1,-1};
    final static int[] dy = {1,-1,0,0};
    ```

    

12. 초기화

    ```java
    boolean[] ck = new boolean[30]; // 기본 false임.
    Arrays.fill(ck, true);          // true로 초기화
    ```

    

13. 클래스

    (노드나 이런걸로 분명 쓰임.)

    ```java
    class Pair {
        int x, y;
        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    ```

    







cf) 자바 int => 4byte => 32bit => 양수/음수 표현 => 2^31 => 0중복 => 2^31-1
