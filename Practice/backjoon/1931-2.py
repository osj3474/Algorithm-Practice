def arrange(sub_lst, answer_lst, id):    # meeting_lst의 일부, 해당 id선택 시의 회의 수, new의 id
    end_time = sub_lst[0][1]
    print("end_time:", end_time)
    for i in range(1,len(sub_lst)):
        print("sub_lst[{}][0]:".format(i), sub_lst[i][0])
        if sub_lst[i][0] >= end_time:
            print("answerid:{} why??".format(id),answer_lst[id])
            return answer_lst[i+id]+1
    return 1

def solution(N, meeting_lst):
    length = len(meeting_lst)
    answer_lst = [1]*length
    for i in range(len(meeting_lst)-1, -1, -1):
        answer_lst[i] = arrange(meeting_lst[i:], answer_lst, i)
        print("answer_lst[{}]:".format(i),answer_lst[i])
        print("")
    print(answer_lst)
    return max(answer_lst)

def main():
    # N = int(input())
    # meeting_lst = [list(map(int, input().split())) for _ in range(N)]

    N = 11
    meeting_lst = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
    meeting_lst.sort()
    print(solution(N, meeting_lst))

main()