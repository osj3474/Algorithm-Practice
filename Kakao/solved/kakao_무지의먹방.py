def solution(food_times, k):
    _sum = sum(food_times)
    if _sum <= k: return -1  # 더 섭취할 음식이 없는 경우 -1 반환

    N = len(food_times)
    food = sorted([[food_times[i], i+1] for i in range(N)], key=lambda x:x[0]) # [food수, 인덱스]

    idx, prev = 0, 0  # idx: 음식 수가 작은 순서로 순차 인덱싱 / prev: 직전 음식 수
    while idx<N:
        temp = (food[idx][0]-prev)*(N-idx)  # 직사각형 넓이를 구하듯이 k감소
        prev = food[idx][0]
        if temp <= k:                       # 해당 직사각형 안에서 정답이 없는 경우
            k -= temp
            for i in range(idx+1, N):
                if food[idx][0] != food[i][0]:
                    idx = i
                    break
        else:                               # 해당 직사각형 안에 정답이 있는 경우
            lst = [food[i][1] for i in range(idx, N)]
            lst.sort()
            return lst[k%(N-idx)]

    return -1

print(solution([3, 1, 2], 5))