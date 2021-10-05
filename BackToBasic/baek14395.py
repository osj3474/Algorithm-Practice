# 이번에 기억할 것 => need에 2가지 속성을 넣는 것을 염려하지 말자
#              => need에 넣기 전에 조건을 검사하자

from collections import deque

MAX = 1000000000

def solution(N, S):
    if N == S: return 0

    need, new_lst = deque(), []
    need.append((N, ""))
    visited = set()

    while need:
        now, op = need.popleft()
        visited.add(now)

        if now == S:
            return op

        nxt = now * now
        if nxt not in visited and 0 <= nxt <= MAX:
            new_lst.append((nxt, op+"*"))

        nxt = now + now
        if nxt not in visited and 0 <= nxt <= MAX:
            new_lst.append((nxt, op+"+"))

        if nxt not in visited :
            new_lst.append((0, op+"-"))

        if now != 0 and nxt not in visited :
            new_lst.append((1, op+"/"))

        if not need:
            need.extend(new_lst)
            new_lst.clear()

    return -1


N, S = map(int, input().split())
print(solution(N, S))