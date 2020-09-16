# 정수 삼각형

<a href="https://programmers.co.kr/learn/courses/30/lessons/43105"> 프로그래머스 고득점 kit DP 2번 </a>



### [ 전략 ]

1. 밑에서부터 위로 올라가면서 매순간 최선의 선택을 한다. (그리디)
2. 마지막의 숫자가 정답이 된다.







![image](https://user-images.githubusercontent.com/42775225/93234900-d900b700-f7b7-11ea-9658-8d13af1650e8.png)















# 입국심사

<a href="https://programmers.co.kr/learn/courses/30/lessons/43238"> 프로그래머스 고득점 kit BS 1번 </a>



### [ 전략 ]

1. 끝낼 수 있는 시간을 기준으로 심사를 시작한다.
2. 끝낼 수 있는 동일 시간에 여러 심사관이 있다면, 시간이 짧은 심사관을 선택한다.
3. 끝내는 시간을 포인팅하고 있기 때문에 n까지 갔다면, 그 때의 시간이 최종 답이 된다.



![image](https://user-images.githubusercontent.com/42775225/93237983-c7b9a980-f7bb-11ea-83c9-076b8f11dbbf.png)

##### [ 코드 ]

```python
import heapq as hq

def solution(n, times):
    minutes = dict()
    for i in range(len(times)):
        minutes[i] = times[i]
        times[i] = [times[i], i]
    hq.heapify(times)

    while 1:
        item = hq.heappop(times)
        n-=1
        if n==0:
            break
        item[0] += minutes[item[1]]
        hq.heappush(times, item)
    return item[0]
```

##### [ 결과 ] 실패 ❌

![image](https://user-images.githubusercontent.com/42775225/93236754-28e07d80-f7ba-11ea-8540-c1cce07bb1b8.png)



### [ BS 로 풀기 ]

### [ 디스커션 ]

통과 인원을 어떻게 O(n) 보다 쉽게 계산할 것인가











# 최단 경로 알고리즘의 이해

### 1. 최단 경로 문제란?

- 최단 경로 문제란 두 노드를 잇는 가장 짧은 경로를 찾는 문제임
- 가중치 그래프 (Weighted Graph) 에서 간선 (Edge)의 가중치 합이 최소가 되도록 하는 경로를 찾는 것이 목적



### 최단 경로 문제 종류

1. 단일 출발 및 단일 도착 (single-source and single-destination shortest path problem) 최단 경로 문제

   - 그래프 내의 특정 노드 u 에서 출발, 또다른 특정 노드 v 에 도착하는 가장 짧은 경로를 찾는 문제

2. 단일 출발 (single-source shortest path problem) 최단 경로 문제

   - 그래프 내의 특정 노드 u 와 그래프 내 다른 모든 노드 각각의 가장 짧은 경로를 찾는 문제

     > 따지고 보면 굉장히 헷깔릴 수 있으므로 명확히 하자면, 예를 들어 A, B, C, D 라는 노드를 가진 그래프에서 특정 노드를 A 라고 한다면, A 외 모든 노드인 B, C, D 각 노드와 A 간에 (즉, A - B, A - C, A - D) 각각 가장 짧은 경로를 찾는 문제를 의미함

3. 전체 쌍(all-pair) 최단 경로: 그래프 내의 모든 노드 쌍 (u, v) 에 대한 최단 경로를 찾는 문제

   

### 2. 최단 경로 알고리즘 - 다익스트라 알고리즘

- 다익스트라 알고리즘은 위의 최단 경로 문제 종류 중, 2번에 해당

  - 하나의 정점에서 다른 모든 정점 간의 각각 **가장 짧은 거리**를 구하는 문제

  

### 다익스트라 알고리즘 로직

- 첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신하는 기법

- 다익스트라 알고리즘은 너비우선탐색(BFS)와 유사

  - 첫 정점부터 각 노드간의 거리를 저장하는 배열을 만든 후, 첫 정점의 인접 노드 간의 거리부터 먼저 계산하면서, 첫 정점부터 해당 노드간의 가장 짧은 거리를 해당 배열에 업데이트

    > 다익스트라 알고리즘의 다양한 변형 로직이 있지만, 가장 개선된 **우선순위 큐**를 사용하는 방식에 집중해서 설명하기로 함

- 우선순위 큐를 활용한 다익스트라 알고리즘

  - 우선순위 큐는 MinHeap 방식을 활용해서, 현재 가장 짧은 거리를 가진 노드 정보를 먼저 꺼내게 됨

  1) 첫 정점을 기준으로 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장

  - 초기에는 첫 정점의 거리는 0, 나머지는 무한대로 저장함 (inf 라고 표현함)
  - 우선순위 큐에 (첫 정점, 거리 0) 만 먼저 넣음

  2) 우선순위 큐에서 노드를 꺼냄

  - 처음에는 첫 정점만 저장되어 있으므로, 첫 정점이 꺼내짐
  - 첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교한다.
  - 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리를 업데이트한다.
  - 배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣는다.
    - 결과적으로 너비 우선 탐색 방식과 유사하게, 첫 정점에 인접한 노드들을 순차적으로 방문하게 됨
    - 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴 거리(루트)를 가진 (노드, 거리)의 경우에는 해당 노드와 인접한 노드간의 거리 계산을 하지 않음

  3) 2번의 과정을 우선순위 큐에 꺼낼 노드가 없을 때까지 반복한다.



![image](https://user-images.githubusercontent.com/42775225/93289589-ad161d80-f819-11ea-9254-0cb4e097ad2a.png)

```python
import heapq

# 탐색할 그래프와 시작 정점을 인수로 전달받습니다.
def dijkstra(graph, start, end):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대(inf)로 초기화합니다.
    distances = {vertex: [float('inf'), start] for vertex in graph}

    # 그래프의 시작 정점의 거리는 0으로 초기화 해줌
    distances[start] = [0, start]

    # 모든 정점이 저장될 큐를 생성합니다.
    queue = []

    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        
        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트합니다.
        current_distance, current_vertex = heapq.heappop(queue)
        
        # 더 짧은 경로가 있다면 무시한다.
        if distances[current_vertex][0] < current_distance:
            continue
            
        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
            if distance < distances[adjacent][0]:
                # 거리를 업데이트합니다.
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])
    
    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print (path_output)
    return distances

# 방향 그래프
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(mygraph, 'A', 'F'))
```

출처 : 패스트 캠퍼스



### [ 이해 해보기 ]

![image](https://user-images.githubusercontent.com/42775225/93296415-1d2c9f80-f82a-11ea-9ddf-90b30b7b0411.png)















