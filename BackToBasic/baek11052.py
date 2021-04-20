N = int(input())
card_lst = list(map(int, input().split()))

def buy(lst, n):
    # 0보다 작은 경우 => fail
    if n<0:
        return False
    # 0인 경우 => finished
    if n==0:
        return True
    # 0보다 큰 경우 => 재귀
    if n>0:
        return buy(lst, n)

# 가능한 조합
# n=4일 경우,
# 1111, 112, 13
# 22
# 4

# n=5일 경우,
# 11111, 1112, 113, 122, 14,
#

# D[n] = N개를 갖기위해 지불해야하는 금액의 최댓값
#      = 