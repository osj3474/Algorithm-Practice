from collections import defaultdict
import heapq as hq

N = int(input())
alpha = [0] * N
M = 0
for i in range(N):
    s = input()
    m = len(s)
    if M < m: M = m
    alpha[i] = list(s)

for i in range(N):
    cnt = M-len(alpha[i])
    if cnt:
        alpha[i] = ['']*cnt + alpha[i]

ver_lst = list(zip(*alpha))
alpha_dict = defaultdict(int)
w = 10**M

for i in range(M):
    for j in range(N):
        if ver_lst[i][j] == '': continue
        alpha_dict[ver_lst[i][j]] += w
    w //= 10

maxh = []
hq.heapify(maxh)

idx = 9
for k, v in alpha_dict.items():
    hq.heappush(maxh, [-v, k])

answer_dict = dict()
for i in range(len(maxh)):
    v, k = hq.heappop(maxh)
    answer_dict[k] = str(idx)
    idx -= 1

total = 0
for i in range(N):
    num = ''
    for j in range(M):
        if alpha[i][j] == '':
            continue
        num += answer_dict[alpha[i][j]]
    total += int(num)

print(total)