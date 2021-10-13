N, M = map(int, input().split())

# 최대 공약수 => 공통 약수 중 가장 큰 정수
gcd = 0
for i in range(1, min(N, M)+1):
    if N%i==0 and M%i==0:
        gcd = i

# 유클리디안
def find_gcd(x, y):
    if y==0:
        return x
    else:
        return find_gcd(y, x%y)

# 최소 공배수 => N*M/gcd
print(gcd)
print(N*M//gcd)