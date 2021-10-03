from collections import deque
from copy import deepcopy as dp

N = int(input())
A = list(input().split())

def oper(S, a, b):
    flag = False
    if (S==">" and a>b) or (S=="<" and a<b):
        flag = True
    return flag

answer_lst = []
fin = N+1
for i in range(10):
    need = deque()
    need.append((i, 0, [i]))  # 수, 연산idx, 과거


    while need:
        now, idx, visited = need.popleft()
        if idx==N:
            answer_lst.append("".join(map(str, visited)))
            continue

        for j in range(10):
            if j in visited: continue

            if oper(A[idx], now, j):
                need.append((j, idx+1, dp(visited)+[j]))

print(max(answer_lst))
print(min(answer_lst))
