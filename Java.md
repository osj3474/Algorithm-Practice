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
   ```

   

5. 딕셔너리 사용하기

   [python]

   ```python
   
   ```

   [java]

   ```java
   
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



















