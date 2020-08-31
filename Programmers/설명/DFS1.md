# 타겟 넘버



<a href="https://programmers.co.kr/learn/courses/30/lessons/43165"> 프로그래머스 고득점 kit DFS1번</a>



### [ 입력 ]

![image-20200826215323422](/Users/osangjin/Library/Application Support/typora-user-images/image-20200826215323422.png)



### [ 출력 ]

![image](https://user-images.githubusercontent.com/42775225/91305964-d4636700-e7e6-11ea-88b0-5ff15d8686bd.png)



### [ 전략 ]

0. 처음에는 경우의 수 문제로 접근 했었으나, 시간초과

   (잠깐 설명하면, [1, 1, 1, 1, 1] --> [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]로 바꾸고, 여기서 모든 경우의 수를 itertools로 구해서 sum 값이 target과 같은지를 비교)



1. 대게 **DFS는 재귀 or 스택** / **BFS는 큐**로 푼다고 합니다. 그런데, 특별한 경우가 아니면, DFS로 풀리는 것은 BFS로 풀리고, BFS로 풀리는 것은 DFS로 풀린다고 합니다.



2. 재귀

   [ 조건 ]

   1) numbers의 갯수 만큼의 element를 모두 사용해야한다.

   2) numbers의 숫자는 -1을 곱한 경우도 사용할 수 있다.

   3) 위 조건의 조합으로 target을 만든다.

   

   [base case]

   numbers의 갯수 만큼의 element를 모두 사용해야하기 때문에 numbers 리스트가 빈 상황에 해당됩니다.

   ![image](https://user-images.githubusercontent.com/42775225/91307535-0c6ba980-e7e9-11ea-81e6-101e801c03fc.png)

   

   [recursive case]

   선택한 숫자는 (이 전에 선택하고 남은 숫자 중) **양수** 혹은 **-1을 곱한 만큼**을 target에서 **빼면서** 재귀를 돌리게 됩니다.

   ![image](https://user-images.githubusercontent.com/42775225/91314302-62dce600-e7f1-11ea-8d3c-ccdcae38777e.png)

