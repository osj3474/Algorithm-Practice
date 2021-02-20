# board와 동일한 크기의 리스트를 2개 만들어서 1개는 각 위치까지 왔을 때, 최대 가치를 담고
# 1개는 각 위치를 방문했는지의 여부를 담는다.
# BFS를 했다. 그런데, BFS임에도 위치를 방문했는지의 여부가 이유는 모르겠는데,
# 글로벌하게 쓰여서 그 부분을 수정하다가 시간을 너무 많이 써서 넘어갔다.

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# memo = [[0]*M for _ in range(N)]   # 방문했는지의 여부

global memo
memo=[[-float('inf')]*M for _ in range(N)]

def tracking(x, y, visited, value):
    print("tracking", x,y)
    if x==N-1 and y==M-1:
        print("value:", value)
        return 1
    global memo
    # 하
    if x+1!=N:
        if visited[x+1][y]==0:
            # print(board[x+1][y], value, ">", memo[x+1][y])
            if board[x+1][y]+value > memo[x+1][y]:
                value += board[x+1][y]
                visited[x+1][y] = 1
                memo[x+1][y] = value
                # print(memo[x+1][y])
                tracking(x+1, y, visited, value)
    # 좌
    if y!=0:
        if visited[x][y - 1]==0:
            # print(2)
            if board[x][y-1]+value > memo[x][y-1]:
                # print(2)
                value += board[x][y-1]
                visited[x][y-1] = 1
                memo[x][y-1] = value
                tracking(x, y-1, visited, value)
    # 우
    if y+1!=N:
        if visited[x][y + 1]==0:
            # print(3)
            # print(board[x][y+1], value, memo[x][y+1])
            if board[x][y+1]+value > memo[x][y+1]:
                # print(3)
                value += board[x][y+1]
                visited[x][y+1] = 1
                memo[x][y+1] = value
                tracking(x, y+1, visited, value)

visited = [[0]*M for _ in range(N)]
tracking(0,0,visited,0)
print(memo)