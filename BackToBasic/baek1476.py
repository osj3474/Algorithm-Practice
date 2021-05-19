E, S, M = map(int, input().split())

E_lst = [15]+[i for i in range(1, 15)]
S_lst = [28]+[i for i in range(1, 28)]
M_lst = [19]+[i for i in range(1, 19)]

i, j, k, answer = 1, 1, 1, 1

while True:
    if i==E and j==S and k==M: break
    i = E_lst[(i+1)%15]
    j = S_lst[(j+1)%28]
    k = M_lst[(k+1)%19]
    answer += 1

print(answer)