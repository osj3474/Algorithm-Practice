S = input()
S_dic = {'d': 10, 'c': 26}
cur = None

answer = 1
for s in S:
    if cur == s:
        answer *= S_dic[s] - 1
    else:
        answer *= S_dic[s]
    cur = s

print(answer)