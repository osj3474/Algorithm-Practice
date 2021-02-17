# bin function 쓰지 않고 풀어보기
T = int(input())
test_lst = [int(input()) for _ in range(T)]

for n in test_lst:
    answer = []
    idx=0
    while(1):
        q, r = divmod(n, 2)
        if r==1:
            answer.append(idx)
        idx += 1
        n = q
        if q==0:
            break
    for i in range(len(answer)):
        print(answer[i], end=" ")
    print()

# bin function을 사용한다면, 참고만 하기
# a=25
# print(list(bin(a))[2:])