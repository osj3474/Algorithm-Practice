N, S = map(int, input().split())
num_lst = list(map(int, input().split()))


def solution(N, S, num_lst):
    MIN = float('inf')

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