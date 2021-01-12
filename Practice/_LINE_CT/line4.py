def move_position(i, j, forward):
    if forward == 0:
        move_lst = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)(i, j+1), (i-1, j), (i, j-1), (i+1, j)]
    return move_lst[forward+1:forward+5]

def makeNewMaze(maze):
    length = len(maze)+2
    board = [[1] * length for _ in range(length)]
    for i in range(1, length-1):
        for j in range(1, length-1):
            board[i][j] = maze[i-1][j-1]
    return board

def solution(maze):
    N = len(maze)
    previous_dic = {0: 2, 1: 3, 2: 0, 3: 1} # E(0), N(1), W(2), S(3)
    previous = 1               # 처음 이전 방향은 막혀있는 North방향으로 초기화
    maze = makeNewMaze(maze)   # 테투리에 1 추가
    total_move = 0
    x, y = 1, 1
    # while x!=N and y!= N:
    forward = 3  # 몇번째 방향인지 (3은 S)
    for i in range(10):
        moves = move_position(x, y, forward)   # E, N, W, S 순으로 좌표를 얻어옴
        cnt = (forward+1) % 4
        print("forward는 {}".format(forward))
        previous = previous_dic[forward]  # 전진한 방향(cnt)의 반대방향을 이전 방향으로 업데이트
        print("previous는 {}".format(previous))
        print("move는 {}".format(moves))
        print("")
        for move in moves:
            # print("previous == cnt:", previous, cnt)
            if previous == cnt:   # 이전 방향과 같으면 해당 방향은 고려 X
                pass
            else:
                i, j = move
                if maze[i][j] != 1:   # 우선순위대로 보고 있으니 1이 아니면 바로 움직여도 됨.
                    x, y = i, j
                    forward = cnt
                    # previous = previous_dic[forward]   # 전진한 방향(cnt)의 반대방향을 이전 방향으로 업데이트
                    print(x, y)
                    # print("previous:", previous)
                    # print("cnt:", cnt)
                    break
            cnt = (cnt + 1) % 4
            # cnt += 1
        total_move += 1
    return total_move

def main():
    maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
    print(solution(maze))

main()