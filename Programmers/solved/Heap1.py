import heapq as hq

def keepGoing(lst, k):  # 스코빌 지수에 미치지 않은 원소가 있는지 확인
    length = len(lst)
    if length > 1:      # 원소가 하나밖에 없으면, 더 섞을 수는 없음
        for i in range(length):
            if lst[i] < k:
                return True  # 더 섞어야 함
    return False

def solution(sco, k):
    hq.heapify(sco)  # min heap 만들기
    cnt = 0          # 섞은 횟수
    while keepGoing(sco, k):      # 섞어야 하는지 확인
        first = hq.heappop(sco)   # 가장 맵지 않은 음식
        second = hq.heappop(sco)  # 두 번째로 맵지 않은 음식
        new = first + second * 2  # 섞은 새로운 음식
        hq.heappush(sco, new)     # heap에 추가
        cnt += 1
    if sco[0] < k:   # 만들 수 없는 경우는 원소가 하나 남은 경우만 확인하면 됨.
        return -1
    return cnt



