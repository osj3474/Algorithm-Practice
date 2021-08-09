n=1
while True:
    if n*n+n>=2000:
        break
    n+=1
t = [0]
for i in range(1, n+1):
    t.extend([i]*i)

A, B = map(int, input().split())
print(sum(t[A:B+1]))