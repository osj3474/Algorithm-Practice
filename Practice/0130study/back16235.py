N, M, K = map(int, input().split())
A_lst = [list(map(int, input().split())) for _ in range(N)]
tree_lst = [list(map(int, input().split())) for _ in range(M)]  # tree의 x,y를 -1씩 하는 걸로
Board_lst = [[5]*N for _ in range(N)]

def make_tree(x, y):
    new_tree = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i==x and j==y) or i<=0 or j<=0 or i>N or j>N:
                continue
            new_tree.append([i, j, 1])
    return new_tree

for _ in range(K):
    # spring
    dead_lst = []
    for tree in tree_lst:
        x, y, z = tree[0]-1, tree[1]-1, tree[2]
        Board_lst[x][y] -= z
        if Board_lst[x][y] < 0:
            dead_lst.append(tree)
            tree_lst.remove(tree)
        tree[2] += 1

    print("Spring")
    print("현재 나무 상태: ", tree_lst)
    print("현재 보드 상태: ", Board_lst)

    # summer
    for dead in dead_lst:
        x, y, z = dead[0]-1, dead[1]-1, dead[2]
        Board_lst[x][y] += z//2

    print("Summer")
    print("현재 나무 상태: ", tree_lst)
    print("현재 보드 상태: ", Board_lst)



    # fall
    for tree in tree_lst:
        x, y, z = tree
        if z%5 == 0:
            tree_lst.extend(make_tree(x-1, y-1))


    print("Fall")
    print("현재 나무 상태: ", tree_lst)
    print("현재 보드 상태: ", Board_lst)



    # winter
    for i in range(N):
        for j in range(N):
            Board_lst[i][j] += A_lst[i][j]

    print("Winter")
    print("현재 나무 상태: ", tree_lst)
    print("현재 보드 상태: ", Board_lst)


print(len(tree_lst))
