# 현재 메모리 초과 / 다시 풀기

import sys
sys.setrecursionlimit(1000000)

n = int(input())

def check(lst, point):
    a, b = point
    left = [a, b-1]
    right = [a, b+1]
    up = [a-1, b]
    down = [a+1, b]
    candidate_lst = [left, right, up, down]
    for element in lst:
        if element in candidate_lst:
            lst = check(lst, lst.pop(0))
    return lst

answers = []
for i in range(n):
    M, N, K = map(int, input().split())
    position_lst = [list(map(int, input().split())) for _ in range(K)]
    total = 0
    while position_lst:
        point = position_lst.pop(0)
        total += 1
        position_lst = check(position_lst, point)
    answers.append(total)

for i in range(len(answers)):
    print(answers[i])