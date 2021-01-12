MAX = 1000000000

def solution(A):
    N = len(A)
    answer_lst = [i for i in range(1, N+1)]
    A.sort()
    total_move = 0
    for i in range(N):
        total_move += abs(A[i]-answer_lst[i])

    if total_move > MAX:
        return -1
    return total_move

def main():
    A = [1]
    print(solution(A))

main()
