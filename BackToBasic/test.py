import math

def my_func(N):
    cnt = 0
    while N!=0:
        dist = int(math.sqrt(N))
        N -= dist*dist
        cnt += 1
    return cnt

def answer_func(n):
    d = [0]*(n+1)
    for i in range(1, n+1):
        d[i] = i
        j = 1
        while j*j <= i:
            if d[i] > d[i-j*j]+1:
                d[i] = d[i-j*j]+1
            j += 1
    return d[n]

for i in range(1, 1000):
    if my_func(i) != answer_func(i):
        print(i)
