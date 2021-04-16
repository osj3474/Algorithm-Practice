MAX = 0
train_cnt = 0

for i in range(10):
    out_cnt, in_cnt = map(int, input().split())
    train_cnt += in_cnt-out_cnt
    if MAX < train_cnt:
        MAX = train_cnt

print(MAX)