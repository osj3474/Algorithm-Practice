

# 자물쇠와 열쇠



<a href="https://programmers.co.kr/learn/courses/30/lessons/60059" target="_blank"> 카카오 3번 </a>



## [ 전략 ]

#### ✅ 변수

- M : 열쇠의 길이
- N : 자물쇠의 길이



#### 1. 자물쇠보다 더 큰 영역을 가정한다. (상하좌우 M-1만큼 증가)

![image](https://user-images.githubusercontent.com/42775225/92557650-a7fc2000-f2a7-11ea-9e67-61d711d85283.png)



#### 2. 열쇠를 옮기면서 열쇠와 자물쇠의 element 합을 구한다.

####  (회전하는 경우까지 각 포인트에서 총 4번의 케이스를 생각한다.)

![image](https://user-images.githubusercontent.com/42775225/92557978-7a63a680-f2a8-11ea-8ec2-32ab9b4d0990.png)



#### 3. lock의 element가 모두 1인지 확인하고, True 혹은 False를 저장하고, 한 번의 True라도 존재하면, True를 리턴한다.







## [ 구현 ]

#### 1. 구현한 함수들

- ##### makeIdx 함수 

  : (1차원 리스트를 기준으로) rotate를 위한 인덱스를 반환하는 함수

- ##### rotate 함수 ✅

  : 1차원 리스트를 넘겨주면, rotate된 1차원 리스트를 반환하는 함수

- ##### makeLongArray 함수

  : 2차원 리스트를 넘겨주면, 1차원 리스트를 반환하는 함수

- ##### MakeMultiArray 함수

  : 1차원 리스트를 넘겨주면, 2차원 리스트를 반환하는 함수

- ##### slidingWindow 함수 ✅

  : key를 이동할 때마다 비교할 element를 추출하는 함수



#### 2. rotate 함수

1차원 기준으로 봤을 때, 인덱스의 나열은 다음과 같은 규칙을 가진다.

![image](https://user-images.githubusercontent.com/42775225/92560114-ca446c80-f2ac-11ea-8423-26feaedfc7c1.png)



![image](https://user-images.githubusercontent.com/42775225/92562222-8f443800-f2b0-11ea-888a-aa43228bad08.png)





#### 3. slidingWindow 함수

![image](https://user-images.githubusercontent.com/42775225/92558387-62405700-f2a9-11ea-91d1-6a3d5a971b07.png)

![image](https://user-images.githubusercontent.com/42775225/92559386-78e7ad80-f2ab-11ea-8ec8-592c9604d3ae.png)





그런데, 열쇠와 자물쇠의 인덱싱도 동일함.

![image](https://user-images.githubusercontent.com/42775225/92559483-a3d20180-f2ab-11ea-8dcc-0ccf2c9daf51.png)



![image](https://user-images.githubusercontent.com/42775225/92559636-f1e70500-f2ab-11ea-8121-d3c77f65aa37.png)





그래서 케이스를 나눠서 slidingWindow 함수 구현.

1) key가 더 큰 경우

![image](https://user-images.githubusercontent.com/42775225/92559327-56559480-f2ab-11ea-9c5c-65811d28cd32.png)





2) key가 더 작은 경우

![image](https://user-images.githubusercontent.com/42775225/92559359-6c635500-f2ab-11ea-91b8-d08a41225faf.png)



3) key가 같은 경우

![image](https://user-images.githubusercontent.com/42775225/92559386-78e7ad80-f2ab-11ea-8ec8-592c9604d3ae.png)











