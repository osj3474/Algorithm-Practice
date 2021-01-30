# 이분탐색
# 시간이 관건
# 그냥 사대마다 모든 동물의 거리를 구하면 바로 탈락될거 같고,
# 동물의 수가 주어지니까 1부터 동물의 수만큼의 리스트를 가지게 해서
# 거기서 binary search하면되지 않을까?

M, N, L = map(int, input().split())
shot_position = list(map(int, input().split()))
animal_lst = [list(map(int, input().split())) for _ in range(N)]

answer_lst = list(range(N))

low = 0
high = N-1
while(low<=high):
    mid = (low+high)//2
    



