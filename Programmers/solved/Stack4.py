import queue


def solution(priorities, location):
    pq = queue.Queue()
    length = len(priorities)
    answer = 0
    
    for i in range(length):
        pq.put((priorities[i], i)) # (우선순위, 인덱스)

    idx = 0
    cnt = 0
        
    while(pq.qsize()):
        printing = pq.get()
        high = max(priorities)
        if printing[0] < high:  # 인쇄 가능 여부
            pq.put((printing))
        else:    
            cnt += 1 # 인쇄 가능
            priorities.remove(high)
            if printing[1] == location:  # 찾던 것과 같은지 확인
                answer = cnt
                break
    return answer
