from collections import deque
import sys

global queue
queue = deque()
global cnt
cnt = 0

def command(S:str):
    global queue
    global cnt
    com = S.split()
    if len(com)==2:
        queue.append(int(com[1]))
        cnt += 1
    if com[0] == 'pop':
        if cnt>0:
            print(queue.popleft())
            cnt -= 1
        else: print(-1)
    elif com[0] == 'size':
        print(cnt)
    elif com[0] == 'empty':
        print(1 if cnt==0 else 0)
    elif com[0] == 'front':
        print(queue[0] if cnt>0 else -1)
    elif com[0] == 'back':
        print(queue[-1] if cnt>0 else -1)

N = int(input())
for _ in range(N):
    command(sys.stdin.readline())

