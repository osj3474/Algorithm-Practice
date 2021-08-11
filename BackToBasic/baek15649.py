N, M = map(int, input().split())

# 순열 구현하기 (재귀)
c = [False]*(N+1)
A = [0]*(N+1)

# m개의 수를 결정하되
# 1~n 까지의 수 중에서
# idx번째 수를 결정하고 있고,
# 다음 idx+1번째 수를 결정해달라고 하면서 끝나는 함수
def go(idx, n, m):
    # 인덱스가 m-1까지만 결정하면 되는데,
    # 결정하려는 수가 m번째라면, 함수 종료
    if idx==m:
        for i in range(m):
            print(A[i], end=' ')
        print()
        return
    # 수를 결정할 때, 항상 1~n까지 모두 돌린다.
    for i in range(1, n+1):
        if c[i]: continue # 이미 선택한 적이 있다면 넘어간다.
        c[i] = True       # i를 선택한다고 말한다.
        A[idx] = i        # 수열에 추가한다.
        go(idx+1, n, m)   # idx+1번째 자리의 수를 결정해달라고 한다.
        c[i] = False      #

go(0, N, M)