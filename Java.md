# 입력

```java
// 입력 (일반 경우)
Scanner sc = new Scanner(System.in);  // ("4.80초")
// EOF까지 입력받기 (입력이 주어지지 않은 경우)
// while(sc.hasNextInt())

// 입력 (많은 경우)
BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // ("0.65초")
```



<br />

# 출력

```java
// 출력 (일반 경우)
System.out.println("30.00초");

// 출력 (많은 경우)
// BufferedWriter ("0.95초");
// StringBuilder  ("1.18초");
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
   
   
   for (Entry<Integer, Integer> e : map.entrySet()) {
     v.add(new Pair(e.getKey(), e.getValue()));
   }
   
   
   
   // 새로운
   map.computeIfPresent(1, (key, value) -> ++value);
   map.putIfAbsent(1, 1);
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
   HashSet<Integer> s = new HashSet<>();
   
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
   s.empty();
   
     
     
   // ====== deque ====== //
   Queue<Integer> q = new LinkedList<Integer>();
   q.add(1);
   q.remove();
   q.isEmpty();
   
   ArrayDeque<Integer> q = new ArrayDeque<Integer>();
   q.add(1);
   q.poll();
   q.addFirst(next);
   q.addLast(next);
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
   
   ```

   

   [java]

   ```java
   ArrayList<Integer> first = new ArrayList<>();
   
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

    

12. 
