# N = int(input())
# meeting_lst = [list(map(int, input().split())) for _ in range(N)]

# memo = {id: depth}
global answer_lst
answer_lst = list()
def arrangeRecur(meeting_lst, id, depth=1, memo={}):
    if id in memo:
        return depth
    print("{}".format('\t'*depth),meeting_lst[id])
    end_time = meeting_lst[id][1]
    isBase = True
    for i in range(id, len(meeting_lst)):
        if meeting_lst[i][0] >= end_time:
            isBase = False
            depth += 1
            arrangeRecur(meeting_lst, i, depth)
            depth -= 1
    if isBase:
        memo[id] = depth
        answer_lst.append(depth)

def solution(N, meeting_lst):
    global answer_lst
    arrangeRecur(meeting_lst, 0)
    print(answer_lst)
    return max(answer_lst)

def main():
    N = int(input())
    meeting_lst = [list(map(int, input().split())) for _ in range(N)]

    # N = 11
    # meeting_lst = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
    print(solution(N, meeting_lst))

main()