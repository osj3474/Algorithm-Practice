N = int(input())
target = int(input())

answer = [[1]*N for _ in range(N)]

i = j = N//2

# 상:i-1 / 하:i+1 / 좌:j-1 / 우:j+1
# N=3, 상1 우1 하2 좌2 상2
# N=5, 상1 우3 하4 좌4 상4

prev = 1
mv_cnt = 1
for _ in range(N//2):
    i -= 1                  # 상1
    answer[i][j] = prev+1
    prev = answer[i][j]

    # 오른쪽 이동
    for _ in range(mv_cnt):
        j += 1
        answer[i][j] = prev+1
        prev = answer[i][j]

    mv_cnt += 1
    # 아래로 이동
    for _ in range(mv_cnt):
        i += 1
        answer[i][j] = prev+1
        prev = answer[i][j]
    # 왼쪽으로 이동
    for _ in range(mv_cnt):
        j -= 1
        answer[i][j] = prev+1
        prev = answer[i][j]
    # 위로 이동
    for _ in range(mv_cnt):
        i -= 1
        answer[i][j] = prev+1
        prev = answer[i][j]
    mv_cnt += 1

p, q = 1, 1
for i in range(N):
    for j in range(N):
        print(answer[i][j], end=' ')
        if answer[i][j] == target:
            p+=i; q+=j
    print()

print(p, q)