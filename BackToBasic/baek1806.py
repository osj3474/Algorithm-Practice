N, S = map(int, input().split())
num_lst = list(map(int, input().split()))


def solution(N, S, num_lst):
    MIN = float('inf')

    # 이렇게 하면 안됩니당~
    # for i in range(N):
    #     total = num_lst[i]
    #     if total==S: return 1
    #     cnt = 1
    #     for j in range(i+1, N):
    #         total += num_lst[j]
    #         cnt += 1
    #         if total >= S:
    #             if MIN > cnt:
    #                 MIN = cnt
    #             break

    # 이렇게 합시당~
    s, e, total = 0, 0, num_lst[0]
    cnt = 1
    while s <= e:
        if total >= S:
            cnt = e - s + 1
            if MIN > cnt: MIN = cnt
            total -= num_lst[s]
            s += 1
        else:
            e += 1
            if e >= N: break
            total += num_lst[e]
    if MIN == float('inf'): MIN = 0
    return MIN


print(solution(N, S, num_lst))

