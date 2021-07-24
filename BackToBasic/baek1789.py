S = int(input())

n = 1
flag =True
S2 = 2*S
while flag:
    if n*n+n>S2: break
    n += 1

print(n-1)
