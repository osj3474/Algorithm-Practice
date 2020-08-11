import heapq as hq

def solution(ops):
    min_heap = [] # heapq 라이브러리를 사용하면 기본이 min_heap

    for op in ops:
        op, digit = op.split(" ")
        digit = int(digit)  # 숫자 파트는 int로
        if op == "I":
            hq.heappush(min_heap, digit)
        if op == "D":
            if min_heap:    # heap에 element가 있어야 동작
                if digit == 1:
                    min_heap.remove(max(min_heap))  # 최댓값은 max로 제거
                    print(1)
                else:
                    hq.heappop(min_heap)   # 최솟값은 min_heap에서 최상위 node
    if min_heap:
        answer = [max(min_heap), hq.heappop(min_heap)]
    else:
        answer = [0, 0]
    return answer
