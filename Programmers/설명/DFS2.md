# 네트워크



<a href="https://programmers.co.kr/learn/courses/30/lessons/43162"> 프로그래머스 고득점 kit DFS2번</a>



### [ 입력 ]

1. 파이썬 코드

![image](https://user-images.githubusercontent.com/42775225/91304777-01167f00-e7e5-11ea-8624-9a5678962e1c.png)





2. 도식

   ![image](https://user-images.githubusercontent.com/42775225/91304989-5357a000-e7e5-11ea-9f53-a7168ec83620.png)

### [ 출력 ]

![image](https://user-images.githubusercontent.com/42775225/91304232-2060dc80-e7e4-11ea-83c2-c0a2555847d0.png)



### [ 전략 ]

1. adjacent list를 만든다.

![image](https://user-images.githubusercontent.com/42775225/91305123-85690200-e7e5-11ea-8b34-290e3f4a65e8.png)



2. 그래프를 탐색하고(BFS), 탐색된 그래프의 노드들은 graph 변수에서 pop한다.

![image](https://user-images.githubusercontent.com/42775225/91305339-e1338b00-e7e5-11ea-9ebb-cd90d5e7cb32.png)



3. 그래프를 탐색하는 횟수를 카운트하고, 최종적으로 출력한다.