N = int(input())
cnt = 0

while N:
    if N%5==0:
        cnt += N//5; break
    elif N>=3:
        cnt += 1
        N -= 3
    else:
        cnt = -1; break

print(cnt)
