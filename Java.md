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

