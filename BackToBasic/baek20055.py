# ========== 일반 리스트 1차 시도 ========== #   > 시간초과
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# belt = list(map(list, list(zip(A, [0]*len(A)))))
#
# def go(lst):
#     return [lst[-1]]+lst[:-1]
#
# n = N-1  # 내리는 위치
# cnt = 0  # 단계 카운트
#
# while K:
#     cnt += 1
#     # 1번
#     belt = go(belt)
#     if belt[n][1] == 1:
#         belt[n][1] = 0
#
#     # 2번
#     for i in range(n-1, -1, -1):
#         if belt[i][1] == 1:  # 로봇이 있으면
#             if belt[i+1][1] != 1 and belt[i+1][0] > 0: # 다음칸 이동 가능하면
#                 belt[i][1] = 0     # 현재칸 로봇 빼고
#                 belt[i+1][1] = 1   # 다음칸 로봇 넣고
#                 belt[i+1][0] -= 1  # 다음칸 내구도 -1
#                 if belt[i+1][0] == 0: K -= 1
#     if belt[n][1] == 1:
#         belt[n][1] = 0
#
#     # 3번
#     if belt[0][1] != 1 and belt[0][0] > 0:
#         belt[0][1] = 1
#         belt[0][0] -= 1
#         if belt[0][0] == 0: K -= 1
#
# print(cnt)




# ========== 링크드 리스트 2차 시도 ========== #  > 시간초과
# class Node:
#     def __init__(self, limit, onRobot, next, prev):
#         self.limit = limit
#         self.onRobot = onRobot
#         self.next = next
#         self.prev = prev
#
# N, K = map(int, input().split())
# node_lst = list(map(lambda x: Node(int(x), 0, None, None), input().split()))
#
# for i in range(1, len(node_lst)-1):
#     node_lst[i].next = node_lst[i+1]
#     node_lst[i].prev = node_lst[i-1]
#
# node_lst[0].prev = node_lst[-1]
# node_lst[0].next = node_lst[1]
# node_lst[-1].next = node_lst[0]
# node_lst[-1].prev = node_lst[-2]
#
# n = N-1 # 내리는 위치
#
# head = node_lst[0]
# tail = node_lst[n]
#
# cnt = 0
#
# while K:
#     cnt += 1
#     # 1번
#     head = head.prev
#     tail = tail.prev
#     if tail.onRobot==1:
#         tail.onRobot = 0
#
#     # 2번
#     now = tail.prev
#     for i in range(N-1):
#         myNext = now.next
#         if now.onRobot == 1:
#             if myNext.onRobot != 1 and myNext.limit > 0:
#                 now.onRobot = 0
#                 myNext.onRobot = 1
#                 myNext.limit -= 1
#                 if myNext.limit == 0: K -= 1
#         now = now.prev
#     if tail.onRobot==1:
#         tail.onRobot = 0
#
#     # 3번
#     if head.onRobot != 1 and head.limit > 0:
#         head.onRobot = 1
#         head.limit -= 1
#         if head.limit == 0: K -= 1
#
# print(cnt)


# 답안지
n, k = map(int, input().split())
a = list(map(int,input().split()))
box = [False] * (2*n)
zero = 0
t = 1
while True:
    a = a[-1:] + a[:-1]
    box = box[-1:] + box[:-1]
    if box[n-1]:
        box[n-1] = False
    for i in range(n-2, -1, -1):
        if box[i]:
            if box[i+1] == False and a[i+1] > 0:
                box[i+1] = True
                box[i] = False
                a[i+1] -= 1
                if a[i+1] == 0:
                    zero += 1
    if box[n-1]:
        box[n-1] = False
    if a[0] > 0:
        box[0] = True
        a[0] -= 1
        if a[0] == 0:
            zero += 1
    if zero >= k:
        print(t)
        break
    t += 1




