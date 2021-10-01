# 11659
# =============== 누적합의 개념을 몰랐을 때  => 실패  ===============

# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split()))
# q_lst = [list(map(lambda x:int(x)-1, sys.stdin.readline().split())) for _ in range(M)]
#
# for s, e in q_lst:
#     print(sum(a[s:e+1]))


# ===============  단순 누적합 편  => 정답  ===============
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split()))
# q_lst = [list(map(lambda x:int(x)-1, sys.stdin.readline().split())) for _ in range(M)]
#
# sum_lst = [0]*N
# sum_lst[0] = a[0]
#
# for i in range(1, N):
#     sum_lst[i] = a[i] + sum_lst[i-1]
#
# for s, e in q_lst:
#     if s==0:
#         print(sum_lst[e])
#     else:
#         print(sum_lst[e]-sum_lst[s-1])


# ===============  세그먼트 트리 편   => 정답  ===============
# 가장 이해 잘 되었던 => https://www.acmicpc.net/blog/view/9
# 리스트의 원소의 갯수가 N이라 했을 때,
#
# 노드의 수    = 2*N-1
# 높이(depth) = ceil(logN)
# 인 이진 트리입니다.

import sys

N, M = map(int, sys.stdin.readline().split())

global a, tree
a = list(map(int, sys.stdin.readline().split()))
tree = [0]*(4*N)

q_lst = [list(map(lambda x:int(x)-1, sys.stdin.readline().split())) for _ in range(M)]


def init(s:int, e:int, n:int): # s=리스트 시작 인덱스, e=리스트 끝 인덱스, n=트리 시작 인덱스
    global a, tree
    if s==e:
        tree[n] = a[s]
    else:
        mid = (s+e)//2
        tree[n] = init(s, mid, n*2) + init(mid+1, e, n*2+1)
    return tree[n]

def acc_sum(s, e, l, r, n): # s=트리 시작 인덱스, e=트리 끝 인덱스, l=구간 첫 인덱스, r=구간 끝 인덱스, n=트리 시작 인덱스
    if l>e or r<s:
        return 0
    if l<=s and e<=r:
        return tree[n]
    mid = (s+e)//2
    return acc_sum(s, mid, l, r, n*2) + acc_sum(mid+1, e, l, r, n*2+1)

init(0, N-1, 1)  # 트리 인덱스는 1로 시작
               # (자식을 찾아갈때, 해당 노드가 x라두면, 좌=2*x / 우=2*x+1 로 연산하기 때문)

for s, e in q_lst:
    print(acc_sum(0, N-1, s, e, 1))