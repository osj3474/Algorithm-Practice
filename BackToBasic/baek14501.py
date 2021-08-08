N = int(input())
task_lst = [list(map(int, input().split())) for _ in range(N)]

# def consult(task_lst, value):
#     length = len(task_lst)
#     for i, task in enumerate(task_lst):
#         if (length-i) >= task[0]:
#             consult(task_lst[i+1:], value)
#     return 1

# def consult(lst):
#     idx, value = lst[0]
#     length = len(lst)
#     if (length - idx) >= task[0]:
#         value += consult(temp_lst)
#     else:
#         return value
#
#     try:
#         temp_lst = lst[idx:]
#         value += consult(temp_lst)
#     except:
#         return 0
#     return value
#     length = len(temp_lst)
#     for i, task in enumerate(temp_lst):
#         if (length-i) >= task[0]:
#             value += consult(temp_lst)
#         else:
#             return value
#     if MAX < value:
#         MAX = value
#
# from collections import defaultdict
#
# def consult(lst, visited=[]):
#     global memo
#     if not lst:
#         return visited
#     idx, value = lst[0]
#     if (idx, value) in memo:
#         visited.append((idx, value))
#         return visited
#     length = len(lst)
#     print()
#     if length-idx < 0:
#         memo[(idx, value)] = 0
#         return visited
#     memo[(idx, value)] = value
#     visited.append((idx, value))
#     for i in range(idx, length):
#         result = consult(lst[idx:], visited)
#         total = 0
#         print("result: ", result)
#         print()
#         # for key in result:
#         #     total += memo[key]
#         # print(total)
#
#
# n = task_lst[0][0]
# global memo
# memo=defaultdict(int)
#
# for i in range(n):
#     consult(task_lst[i:])
#
# print(memo)

N = int(input())
t, p = [0]*(N+1), [0]*(N+1)
for i in range(1, N+1):
    t[i], p[i] = map(int, input().split())

global MAX
MAX = 0

def consult(d, s):
    global MAX
    if d==N+1:
        if MAX < s: MAX = s
        return
    if d>N+1: return
    consult(d+t[d], s+p[d])
    consult(d+1, s)

consult(1, 0)
print(MAX)