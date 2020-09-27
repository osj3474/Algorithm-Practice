# 가장 먼 노드

<a href="https://programmers.co.kr/learn/courses/30/lessons/49189"> 프로그래머스 고득점 kit Graph 1번 </a>



### [ 전략 ]

1. 1번 노드로 부터의 거리의 정보를 담은 리스트를 만들고, 초기값을 Inf로 설정한다.

   ![image](https://user-images.githubusercontent.com/42775225/93968474-a1d86a00-fda4-11ea-902d-a0fd97a7bc56.png)

2. queue에서 꺼낸 노드의 인접 노드의 거리를 보고, 더 크면 짧은 거리로 업데이트 한다.

   ![image](https://user-images.githubusercontent.com/42775225/93968635-0b587880-fda5-11ea-9efd-690ea63aab1c.png)



3. 모든 노드의 거리가 업데이트 되면, 가장 긴 거리에 해당하는 노드의 갯수를 정답으로 출력한다.

   ##### [결과]

   ```
   [0, 0, 1, 1, 2, 2, 2]
   ```

   



### [ 사용된 알고리즘 ]

#### ⭐️ BFS

```python
from collections import deque
def BFS(graph, start_node):
    need, visited = deque(), list()
    need.append(start_node)
    while need:
        now = need.popleft()
        if now not in visited:
            visited.append(now)
            need.extend(graph[now])
    return visited
```





















# 입국심사

<a href="https://programmers.co.kr/learn/courses/30/lessons/43238"> 프로그래머스 고득점 kit BS 1번 </a>



### [ 전략 ]

1. 이분 탐색할 대상이 되는 리스트는 정답 후보에 해당하는, 시간정보 '분' 이 된다.

2. 해당 리스트에서 이분 탐색하면서, 문제에서 요구하는 n명의 사람의 심사 통과를 확인한다.

   (단, 여기서 이분 탐색 종료 조건은 정확한 n 값이 아니다. 왜냐하면, 다음의 그림에서 만들 수 있는 값은 1, 3, 4, 7, 8, 10만 가능하다.)

   (해당 부분을 alpha라 두고 오차까지 포함한 값에 해당되면 탐색을 종료한다.)

   



![image](https://user-images.githubusercontent.com/42775225/93976294-be2fd300-fdb3-11ea-9a0c-4e7a4aca120a.png)







### [ 코드 ]

```python
def solution(n, times):
    length = len(times)
    MAX = n*max(times)
    minute_lst = [i for i in range(1, MAX+1)]
    low = 0
    high = len(minute_lst)
    while low<=high:
        mid = (low+high) // 2
        total, alpha = 0, 0
        for i in range(length):
            total += minute_lst[mid]//times[i]
            if minute_lst[mid] % times[i]:
                alpha += 1
        ck_lst = [i for i in range(total-alpha, total+1)]
        if n in ck_lst:
            break
        elif total > n:
            high = mid-1
        else:
            low = mid+1
    return minute_lst[mid]
```

























