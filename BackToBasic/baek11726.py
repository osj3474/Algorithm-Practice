import sys
sys.setrecursionlimit(1000000)

n = int(input())
global memo
memo = [0]*1001

# D[n] = D[n-1] + D[n-2]
# 1 : 1
# 2 : 2
def combi(n):
    global memo
    if n<=2:
        return n
    if memo[n] > 0:
        return memo[n]
    memo[n] = combi(n-1)+combi(n-2)
    return memo[n]

print(combi(n))