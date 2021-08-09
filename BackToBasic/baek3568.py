S = input().split()
N = len(S)
for i in range(1, N):
    S[i] = S[i][:-1]
    temp = ''
    idx=0
    j = len(S[i])-1
    while j>0:
        if S[i][j]=='&' or S[i][j]=='*':
            temp+=S[i][j]
            j-=1
        elif S[i][j-1:j+1] == '[]':
            temp+=S[i][j-1:j+1]
            j-=2
        else:break

    print(S[0]+temp, S[i][:j+1]+';')
