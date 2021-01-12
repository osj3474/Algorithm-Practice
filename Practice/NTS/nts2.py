def plus(n):
    return n*(n+1)//2

def solution(N):
    answer = N      # 모든 N에 대하여 최소로 가지는 값(맞은편 1 + 둘로 묶었을 때 N-1)
    i = 2
    while 1:
        pair = 2**i # 4,8,16,32,...
        if N//pair: # N >= 4, N//4 > 0
            cnt = N-pair+1
            answer += plus(cnt)
        else:
            break
        i+=1
    return answer

def main():
    N = 6
    print(solution(N))

main()