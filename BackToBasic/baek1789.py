S = int(input())

n = 1
S2 = 2*S
while 1:
    if n*n+n>S2: break
    n += 1

print(n-1)
