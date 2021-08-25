class Node:
    def __init__(self, limit, onRobot, next, prev):
        self.limit = limit
        self.onRobot = onRobot
        self.next = next
        self.prev = prev

N, K = map(int, input().split())
node_lst = list(map(lambda x: Node(int(x), 0, None, None), input().split()))

for i in range(1, len(node_lst)-1):
    node_lst[i].next = node_lst[i+1]
    node_lst[i].prev = node_lst[i-1]

node_lst[0].prev = node_lst[-1]
node_lst[0].next = node_lst[1]
node_lst[-1].next = node_lst[0]
node_lst[-1].prev = node_lst[-2]

n = N-1 # 내리는 위치

head = node_lst[0]
tail = node_lst[n]

cnt = 0

while K:
    cnt += 1
    # 1번
    head = head.prev
    tail = tail.prev
    if tail.onRobot==1:
        tail.onRobot = 0

    # 2번
    now = tail.prev
    for i in range(N-1):
        myNext = now.next
        if now.onRobot == 1:
            if myNext.onRobot != 1 and myNext.limit > 0:
                now.onRobot = 0
                myNext.onRobot = 1
                myNext.limit -= 1
                if myNext.limit == 0: K -= 1
        now = now.prev
    if tail.onRobot==1:
        tail.onRobot = 0

    # 3번
    if head.onRobot != 1 and head.limit > 0:
        head.onRobot = 1
        head.limit -= 1
        if head.limit == 0: K -= 1

print(cnt)