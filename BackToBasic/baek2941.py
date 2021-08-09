my_dic = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}
S = input()
length = len(S)

cnt = 0
i = 0
while i<length:
    if i<=length-3:
        if S[i:i+2] in my_dic: i += 2
        elif S[i:i+3] in my_dic: i += 3
        else: i+=1
    else:
        if i==length-1:
            i+=1; cnt+=1
            continue
        if S[i:i+2] in my_dic: i+=2
        else: i+=1
    cnt += 1

print(cnt)