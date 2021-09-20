# 통과는 했지만, 정답은 참고하기
global cnt_set
cnt_set = set()

N, S = map(int, input().split())
a = list(map(int, input().split()))

def go(total, i, prev=[]):
    # print('{} total={}, lst={}'.format('  '*depth, total, lst))
    global cnt_set
    if total==S and prev:
        cnt_set.add(tuple(prev))
    if i>=N: return
    go(total+a[i], i+1, prev+[i])
    go(total, i+1, prev)


for i in range(N):
    go(0, i)

print(len(cnt_set))



## 정답
# n = int(input())
# a = list(map(int,input().split()))
# c = [False]*(n*100000+10)
# def go(i, sum):
#     if i == n:
#         c[sum] = True
#         return
#     go(i+1,sum+a[i])
#     go(i+1,sum)
# go(0,0)
# i = 1
# while True:
#     if c[i] == False:
#         break
#     i += 1
# print(i)