# 베스트 앨범 

<a href="https://programmers.co.kr/learn/courses/30/lessons/42579" target="_blank">프로그래머스 고득점kit 해시 4번 문제</a>



### [ 입력 ]

![image](https://user-images.githubusercontent.com/42775225/91274456-ad427080-e7b9-11ea-9fc3-89d05ddcf654.png)





### [ 출력 ]

![image](https://user-images.githubusercontent.com/42775225/91314501-9881cf00-e7f1-11ea-8e23-c92e6ad2520d.png)



### [ 전략 ]

#### 1) 목적에 맞는 자료형으로 필요한 정보를 담은 변수를 만듭니다.



![image](https://user-images.githubusercontent.com/42775225/91274548-cfd48980-e7b9-11ea-85cb-3e8b55d9ef75.png)



1. genre_dic 

   **인덱스** 와 **플레이 수** 의 정보를 **장르** 별로 담은 **dictionary** 

   (인덱스와 플레이 수 정보는 바뀌지 않기 때문에 tuple 선택, key에 따른 value 형식이라서 dictionary 선택)

2. play_cnt_lst

   **장르** 별 총 **플레이 합계**의 정보를 담은 **list**

   (정렬을 위해 list 자료형을 선택)



#### 2) 1개만 있는 경우를 예외처리해서 출력해 줍니다.

```python
answer.append(genre_dic[genre][0][0])
try:
  answer.append(genre_dic[genre][1][0])
except:
    pass
```

