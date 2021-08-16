import math

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    if N < M: N, M = M, N
    print(math.factorial(N)//math.factorial(M)//math.factorial(N-M))