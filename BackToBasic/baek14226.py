from collections import deque

S = int(input())

need, new, visited = deque(), list(), set()
need.append((1, 0))
cnt = 0

while need:
    v, c = need.popleft()
    if v == S: break
    if v in visited: continue
    for k in [(v, v), (v+c, c), (v-1, c)]:
        if k[0]<0 or k[0]>2000 or k in visited: continue
        new.append(k)
        visited.add(k)
    if not need:
        cnt += 1
        need.extend(new)
        new.clear()

print(cnt)