N = int(input())
a = list(map(int, input().split()))

answer_lst = [-1]*len(a)
pocket = []

prev = a[0]
idx = 0
pocket.append((prev, idx))

for i in range(1, N):
    if a[i] <= prev:
        pocket.append((prev, idx))
    else:    # 더 큰걸 찾은 상황
        answer_lst[idx] = a[i]
        for j in range(len(pocket)-1, -1, -1):
            if pocket[j][0] < a[i]:
                answer_lst[pocket[j][1]] = a[i]
                pocket.pop()
            else: break
    prev = a[i]
    idx = i

for i in range(N):
    print(answer_lst[i], end=" ")