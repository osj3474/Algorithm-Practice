n_lst = input()
toggle_cnt = [1, 0]
flag = 0
for i in range(len(n_lst)-1):
    if n_lst[i] != n_lst[i+1]:
        flag += 1
        toggle_cnt[flag % 2] += 1
print(min(toggle_cnt))