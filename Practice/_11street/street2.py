from collections import defaultdict

def solution(S):
    M = len(S[0])
    N = len(S)
    row1, row2, col = 0, 0, 0
    for c in range(M):
        alpha_dic = defaultdict(int)
        for r in range(N):
            alpha_dic[S[r][c]] += 1
            if alpha_dic[S[r][c]] == 2:
                row2, col = r, c
                break

    for i in range(row2):
        if S[i][col] == S[row2][col]:
            row1 = i
            break
    answer = [row1, row2, col]
    if answer == [0,0,0]:
        answer = []
    return answer

def main():
    S = ["aze"]
    print(solution(S))

main()
