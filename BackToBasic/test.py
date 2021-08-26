N = str(input())

lis = [i for i in range(10)]
count = 1

for cnt in range(len(N)):
    if int(N[cnt]) in lis:
        lis.remove(int(N[cnt]))
    elif int(N[cnt]) == 6:
        if 9 in lis:
            lis.remove(9)
        else:
            count += 1
            lis = [i for i in range(10)]
            lis.remove(int(N[cnt]))
    elif int(N[cnt]) == 9:
        if 6 in lis:
            lis.remove(6)
        else:
            count += 1
            lis = [i for i in range(10)]
            lis.remove(int(N[cnt]))
    else:
        count += 1
        lis = [i for i in range(10)]
        lis.remove(int(N[cnt]))
print(count)





