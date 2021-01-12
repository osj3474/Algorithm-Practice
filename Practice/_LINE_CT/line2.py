def solution(balls, orders):
    length = len(balls)
    out_lst = [0]*length    # 빠져나가는 순서를 담은 리스트
    idx = 0                 # out_lst의 인덱스
    waiting_dic = dict()    # 공의 번호를 key로 가지며, 기다리고 있는지를 boolean으로 나타내는 딕셔너리
    for ball in balls:      # order는 있었지만 막혀서 나오지 못한 공은 True, 나머지는 False
        waiting_dic[ball] = False
    i, j = 0, length-1      # 리스트의 처음 인덱스(i), 끝 인덱스(j)
    for order in orders:
        if balls[i] == order:        # 맨앞 공과 order가 같은 경우
            out_lst[idx] = balls[i]  # 해당 공의 정보를 out_lst 에 넣는다.
            idx += 1
            i += 1
            while waiting_dic[balls[i]]:       # 공을 업데이트 했는데, 기다리던 공이면, 해당 공도 out_lst에 넣는다.
                waiting_dic[balls[i]] = False
                out_lst[idx] = balls[i]
                idx += 1
                i += 1
        elif balls[j] == order:      # 맨끝 공과 order가 같은 경우
            out_lst[idx] = balls[j]  # 해당 공의 정보를 out_lst 에 넣는다.
            idx += 1
            j -= 1
            while waiting_dic[balls[j]]:
                waiting_dic[balls[j]] = False
                out_lst[idx] = balls[j]
                idx += 1
                j -= 1
        else:
            waiting_dic[order] = True
    return out_lst

def main():
    ball = [11, 2, 9, 13, 24]
    order = [9, 2, 13, 24, 11]
    print(solution(ball, order))

main()