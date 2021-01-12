N, d = map(int, input().split())
bomb_lst = [0] * N
for i in range(N):
	bomb_lst[i] = list(map(int, input().split()))

print(N, d, bomb_lst)