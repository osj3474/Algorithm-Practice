N, k = map(int, input().split())
strength_lst = list(map(int, input().split()))
path_lst = [list(map(int, input().split())) for _ in range(k)]

print(N, k, strength_lst, path_lst)