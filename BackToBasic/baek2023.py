# 소수 ==> 에라토스테네스의 체 가 정석이라고 생각했는데,
# 그런데 메모리 제한이 있어서 불가능했고,
# 매번 숫자를 검사하되, 최대한 검사할 숫자의 범위를 줄이는 것이 중요했다.
# 1 자리수 : 2, 3, 5, 7
# 마지막 자리수 : 최소 홀수여야함
# https://kimmeh1.tistory.com/353 ==> 너무 잘 푸셔서 가져옴.

N = int(input())
heads = ['2', '3', '5', '7']
tails = ['1', '3', '5', '7', '9']

def isPrime(n):
    if n==1: return False

    end = int(n**(1/2))+1
    for i in range(2, end):
        if n%i == 0:
            return False
    return True


def find_amazing(num):
    if len(num)==N:
        print(num)
        return

    for t in tails:
        if isPrime(int(num+t)):
            find_amazing(num+t)

for h in heads:
    find_amazing(h)
