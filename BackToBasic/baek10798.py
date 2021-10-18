entire_lst = []
max_length = 0

for _ in range(5):
    temp = list(input())
    if max_length < len(temp):
        max_length = len(temp)
    entire_lst.append(temp)

for i in range(max_length):
    for j in range(len(entire_lst)):
        try:
            print(entire_lst[j][i], end='')
        except:
            pass
