N = int(input())
time_lst = [0]*N

for i in range(N):
    t, n, *a = map(int, input().split())

    _max = 0
    for idx in a:
        if _max < time_lst[idx-1]:
            _max = time_lst[idx-1]
    time_lst[i] = _max + t

print(max(time_lst))