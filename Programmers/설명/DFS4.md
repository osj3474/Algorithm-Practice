# 여행 경로



<a href="https://programmers.co.kr/learn/courses/30/lessons/43164"> 프로그래머스 고득점 kit DFS 4</a>



### [ 입력 ]

![image](https://user-images.githubusercontent.com/42775225/91673311-9495da00-eb6e-11ea-8030-510749d6eee2.png)



### [ 출력 ]

![image](https://user-images.githubusercontent.com/42775225/91673396-e5a5ce00-eb6e-11ea-9389-e23c2536279c.png)



### [ 전략 ]

1. 조건에 맞는 여행경로가 2개 이상 나올 수 있기 때문에, 이를 저장할 리스트를 전역 변수로 생성

   ```python
   def solution(tickets):
       global answer_lst      # 정답이 되는 케이스를 모아둘 리스트 생성
       answer_lst = list()
       travel(tickets, "ICN") # 항상 시작은 ICN에서 시작됨.
   ```

   

2. 티켓을 모두 소진한 경우를 base case로 설정 (정답 리스트에 추가)

   ```python
   if not tickets:    # 티켓을 모두 소진했다는 것은 정답이 될 수 있는 경우
     temp = travel_lst[:]      # shallow copy이지만, iterable 객체가 없기 때문에, deep copy와 같음.
     answer_lst.append(temp)   # 복사본을 수정해도 원본에는 타격없음.
     return 1
   ```



3. 티켓을 하나 선택할 때마다 새로운 후보군을 찾고, 각 후보에 대해 다시 재귀함수 실행

   ```python
   candidate_lst = findCandidate(tickets, start)  # 후보군 생성  // O(N)
   if candidate_lst:  # 후보군이 있는 경우만
     for candidate in candidate_lst:      # // O(N)
       last = tickets[:]
       last.remove(candidate)           # ticket 업데이트
       travel_lst.append(candidate[1])  # 여행경로 업데이트
       travel(last, candidate[1], travel_lst)  # 다시 여행 // O(N)
       travel_lst.pop()  # 후보군이 없거나, 티켓 소진시 한칸 이전 상태로 복귀
   ```

   

4. 최종 정답 출력

   ```python
   answer_lst.sort()      # 알파벳 순서가 앞서는 경로를 반환해야함.
   answer = answer_lst[0]
   return answer
   ```

   



### [ 시간 복잡도 ]

![image](https://user-images.githubusercontent.com/42775225/91673618-ec811080-eb6f-11ea-9fcd-a990ac6d81fa.png)