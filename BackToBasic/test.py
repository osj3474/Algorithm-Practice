N, K = map(int, input().split())
A = list(map(int, input().split()))
belt = list(map(list, list(zip(A, [0]*len(A)))))

def go(lst):
    return [lst[-1]]+lst[:-1]

n = N-1  # 내리는 위치
cnt = 0  # 단계 카운트

while K:
    cnt += 1
    # 1번
    belt = go(belt)
    if belt[n][1] == 1:
        belt[n][1] = 0

    # 2번
    for i in range(n-1, -1, -1):
        if belt[i][1] == 1:  # 로봇이 있으면
            if belt[i+1][1] != 1 and belt[i+1][0] > 0: # 다음칸 이동 가능하면
                belt[i][1] = 0     # 현재칸 로봇 빼고
                belt[i+1][1] = 1   # 다음칸 로봇 넣고
                belt[i+1][0] -= 1  # 다음칸 내구도 -1
                if belt[i+1][0] == 0: K -= 1
    if belt[n][1] == 1:
        belt[n][1] = 0

    # 3번
    if belt[0][1] != 1 and belt[0][0] > 0:
        belt[0][1] = 1
        belt[0][0] -= 1
        if belt[0][0] == 0: K -= 1

print(cnt)